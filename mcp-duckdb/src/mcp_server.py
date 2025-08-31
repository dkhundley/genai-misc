#!/usr/bin/env python3
"""
DuckDB MCP Server

A Model Context Protocol server that provides natural language querying capabilities
for a DuckDB database containing Netflix data.
"""


import asyncio
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import duckdb
import openai
import polars as pl
import yaml
from mcp.server.fastmcp import FastMCP
from mcp.types import Resource, Tool, TextContent, ImageContent, EmbeddedResource, LoggingLevel
from pydantic import AnyUrl

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("duckdb-mcp-server")

mcp = FastMCP("duckdb-mcp-server")
connection: Optional[duckdb.DuckDBPyConnection] = None
openai_client: Optional[openai.OpenAI] = None

async def initialize_database():
    global connection
    current_dir = Path(__file__).parent
    app_root = current_dir.parent
    data_path = app_root / "data" / "netflix_data.csv"
    connection = duckdb.connect(database=":memory:", read_only=False)
    if data_path.exists():
        df_netflix = pl.read_csv(str(data_path))
        connection.register("netflix", df_netflix)
        logger.info(f"Loaded Netflix data with {len(df_netflix)} rows")
    else:
        raise FileNotFoundError(f"Netflix data file not found: {data_path}")

async def initialize_openai():
    global openai_client
    app_root = Path(__file__).parent.parent.parent
    keys_path = app_root / "keys" / "api_keys.yaml"
    print(f"DEBUG: Looking for API keys file at: {keys_path}, exists: {keys_path.exists()}")
    if keys_path.exists():
        with open(keys_path) as f:
            api_keys = yaml.safe_load(f)
        openai_client = openai.OpenAI(api_key=api_keys['OPENAI_API_KEY'])
        logger.info("OpenAI client initialized")
    else:
        raise FileNotFoundError(
            f"API keys file not found: {keys_path}\n"
            "Please create the file with the following format:\n"
            "OPENAI_API_KEY: <your-openai-api-key>\n"
        )

@mcp.prompt()
def create_sql_prompt(schema: str, question: str) -> str:
    return f"""You are an expert DuckDB SQL analyst. Generate a valid SQL query to answer the user's question.

IMPORTANT: Return ONLY the SQL query, no explanations or formatting.

Database Schema:
{schema}

User Question: {question}

SQL Query:"""

@mcp.tool()
async def query_netflix_data(question: str) -> List[TextContent]:
    if not connection or not openai_client:
        raise RuntimeError("Server not properly initialized")
    schema_df = connection.execute("DESCRIBE netflix;").fetchdf()
    schema_str = schema_df.to_string(index=False)
    prompt = create_sql_prompt(schema_str, question)
    response = await asyncio.get_event_loop().run_in_executor(
        None,
        lambda: openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a SQL expert. Generate only valid SQL queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=500
        )
    )
    sql_query = response.choices[0].message.content.strip()
    if sql_query.startswith("```"):
        sql_query = sql_query.split('\n', 1)[1]
    if sql_query.endswith("```"):
        sql_query = sql_query.rsplit('\n', 1)[0]
    results_df = connection.execute(sql_query).fetchdf()
    if len(results_df) > 0:
        result_json = results_df.to_json(orient="records", indent=2)
        return [TextContent(type="text", text=f"Generated SQL:\n{sql_query}\n\nResults ({len(results_df)} rows):\n{result_json}")]
    else:
        return [TextContent(type="text", text=f"Generated SQL:\n{sql_query}\n\nNo results found.")]

@mcp.tool()
async def get_schema() -> List[TextContent]:
    if not connection:
        raise RuntimeError("Database not initialized")
    schema_df = connection.execute("DESCRIBE netflix;").fetchdf()
    schema_json = schema_df.to_json(orient="records", indent=2)
    return [TextContent(type="text", text=f"Netflix Database Schema:\n{schema_json}")]

@mcp.tool()
async def execute_sql(sql: str) -> List[TextContent]:
    if not connection:
        raise RuntimeError("Database not initialized")
    results_df = connection.execute(sql).fetchdf()
    if len(results_df) > 0:
        result_json = results_df.to_json(orient="records", indent=2)
        return [TextContent(type="text", text=f"Query executed successfully ({len(results_df)} rows):\n{result_json}")]
    else:
        return [TextContent(type="text", text="Query executed successfully. No results found.")]

@mcp.resource()
async def list_resources() -> List[Resource]:
    return [
        Resource(
            uri=AnyUrl("netflix://schema"),
            name="Netflix Database Schema",
            description="Schema information for the Netflix dataset",
            mimeType="application/json"
        ),
        Resource(
            uri=AnyUrl("netflix://sample"),
            name="Netflix Sample Data",
            description="Sample rows from the Netflix dataset",
            mimeType="application/json"
        )
    ]

@mcp.resource()
async def read_resource(uri: AnyUrl) -> str:
    if not connection:
        raise RuntimeError("Database not initialized")
    if str(uri) == "netflix://schema":
        schema_df = connection.execute("DESCRIBE netflix;").fetchdf()
        return schema_df.to_json(orient="records", indent=2)
    elif str(uri) == "netflix://sample":
        sample_df = connection.execute("SELECT * FROM netflix LIMIT 5;").fetchdf()
        return sample_df.to_json(orient="records", indent=2)
    else:
        raise ValueError(f"Unknown resource: {uri}")

async def main():
    await initialize_database()
    await initialize_openai()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    asyncio.run(main())
