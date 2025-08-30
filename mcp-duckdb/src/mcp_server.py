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
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)
from pydantic import AnyUrl

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("duckdb-mcp-server")

class DuckDBMCPServer:
    """MCP Server for DuckDB natural language queries."""
    
    def __init__(self):
        self.server = Server("duckdb-mcp-server")
        self.connection: Optional[duckdb.DuckDBPyConnection] = None
        self.openai_client: Optional[openai.OpenAI] = None
        
        # Setup handlers
        self._setup_handlers()
        
    def _setup_handlers(self):
        """Set up all MCP handlers."""
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="query_netflix_data",
                    description="Execute natural language queries against the Netflix database",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "question": {
                                "type": "string",
                                "description": "Natural language question about the Netflix data"
                            }
                        },
                        "required": ["question"]
                    }
                ),
                Tool(
                    name="get_schema",
                    description="Get the schema information for the Netflix database",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                Tool(
                    name="execute_sql",
                    description="Execute a SQL query directly against the Netflix database",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "sql": {
                                "type": "string",
                                "description": "SQL query to execute"
                            }
                        },
                        "required": ["sql"]
                    }
                )
            ]

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Handle tool calls."""
            try:
                if name == "query_netflix_data":
                    return await self._query_netflix_data(arguments.get("question", ""))
                elif name == "get_schema":
                    return await self._get_schema()
                elif name == "execute_sql":
                    return await self._execute_sql(arguments.get("sql", ""))
                else:
                    raise ValueError(f"Unknown tool: {name}")
                    
            except Exception as e:
                logger.error(f"Error handling tool call {name}: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

        @self.server.list_resources()
        async def handle_list_resources() -> List[Resource]:
            """List available resources."""
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

        @self.server.read_resource()
        async def handle_read_resource(uri: AnyUrl) -> str:
            """Read resource content."""
            try:
                if str(uri) == "netflix://schema":
                    return await self._get_schema_resource()
                elif str(uri) == "netflix://sample":
                    return await self._get_sample_data()
                else:
                    raise ValueError(f"Unknown resource: {uri}")
            except Exception as e:
                logger.error(f"Error reading resource {uri}: {e}")
                return f"Error: {str(e)}"

    async def _initialize_database(self) -> None:
        """Initialize the DuckDB connection and load data."""
        try:
            # Setup paths
            current_dir = Path(__file__).parent
            app_root = current_dir.parent
            data_path = app_root / "data" / "netflix_data.csv"
            
            # Connect to DuckDB
            self.connection = duckdb.connect(database=":memory:", read_only=False)
            
            # Load Netflix data
            if data_path.exists():
                df_netflix = pl.read_csv(str(data_path))
                self.connection.register("netflix", df_netflix)
                logger.info(f"Loaded Netflix data with {len(df_netflix)} rows")
            else:
                raise FileNotFoundError(f"Netflix data file not found: {data_path}")
                
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise

    async def _initialize_openai(self) -> None:
        """Initialize OpenAI client."""
        try:
            # Setup correct path for API keys
            app_root = Path(__file__).parent.parent.parent  # Go up two levels to repo root
            keys_path = app_root / "keys" / "api_keys.yaml"
            print(f"DEBUG: Looking for API keys file at: {keys_path}, exists: {keys_path.exists()}")
            
            # Load API keys
            if keys_path.exists():
                with open(keys_path) as f:
                    api_keys = yaml.safe_load(f)
                self.openai_client = openai.OpenAI(api_key=api_keys['OPENAI_API_KEY'])
                logger.info("OpenAI client initialized")
            else:
                # Improved error message with instructions
                raise FileNotFoundError(
                    f"API keys file not found: {keys_path}\n"
                    "Please create the file with the following format:\n"
                    "OPENAI_API_KEY: <your-openai-api-key>\n"
                )
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise

    def _create_sql_prompt(self, schema: str, question: str) -> str:
        """Create a prompt for SQL generation."""
        return f"""You are an expert DuckDB SQL analyst. Generate a valid SQL query to answer the user's question.

IMPORTANT: Return ONLY the SQL query, no explanations or formatting.

Database Schema:
{schema}

User Question: {question}

SQL Query:"""

    async def _query_netflix_data(self, question: str) -> List[TextContent]:
        """Execute a natural language query against Netflix data."""
        if not self.connection or not self.openai_client:
            raise RuntimeError("Server not properly initialized")
            
        try:
            # Get schema
            schema_df = self.connection.execute("DESCRIBE netflix;").fetchdf()
            schema_str = schema_df.to_string(index=False)
            
            # Generate SQL using OpenAI
            prompt = self._create_sql_prompt(schema_str, question)
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.openai_client.chat.completions.create(
                    model="gpt-4o-mini",  # Use more cost-effective model
                    messages=[
                        {"role": "system", "content": "You are a SQL expert. Generate only valid SQL queries."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0,
                    max_tokens=500
                )
            )
            
            sql_query = response.choices[0].message.content.strip()
            
            # Clean up the SQL query (remove any markdown formatting)
            if sql_query.startswith("```"):
                sql_query = sql_query.split('\n', 1)[1]
            if sql_query.endswith("```"):
                sql_query = sql_query.rsplit('\n', 1)[0]
            
            # Execute the query
            results_df = self.connection.execute(sql_query).fetchdf()
            
            # Format results
            if len(results_df) > 0:
                result_json = results_df.to_json(orient="records", indent=2)
                return [TextContent(
                    type="text",
                    text=f"Generated SQL:\n{sql_query}\n\nResults ({len(results_df)} rows):\n{result_json}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"Generated SQL:\n{sql_query}\n\nNo results found."
                )]
                
        except Exception as e:
            logger.error(f"Error in natural language query: {e}")
            raise RuntimeError(f"Query failed: {str(e)}")

    async def _get_schema(self) -> List[TextContent]:
        """Get the database schema information."""
        if not self.connection:
            raise RuntimeError("Database not initialized")
            
        try:
            schema_df = self.connection.execute("DESCRIBE netflix;").fetchdf()
            schema_json = schema_df.to_json(orient="records", indent=2)
            
            return [TextContent(
                type="text",
                text=f"Netflix Database Schema:\n{schema_json}"
            )]
            
        except Exception as e:
            logger.error(f"Error getting schema: {e}")
            raise RuntimeError(f"Failed to get schema: {str(e)}")

    async def _execute_sql(self, sql: str) -> List[TextContent]:
        """Execute a SQL query directly."""
        if not self.connection:
            raise RuntimeError("Database not initialized")
            
        try:
            results_df = self.connection.execute(sql).fetchdf()
            
            if len(results_df) > 0:
                result_json = results_df.to_json(orient="records", indent=2)
                return [TextContent(
                    type="text",
                    text=f"Query executed successfully ({len(results_df)} rows):\n{result_json}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text="Query executed successfully. No results found."
                )]
                
        except Exception as e:
            logger.error(f"Error executing SQL: {e}")
            raise RuntimeError(f"SQL execution failed: {str(e)}")

    async def _get_schema_resource(self) -> str:
        """Get schema as a resource."""
        if not self.connection:
            raise RuntimeError("Database not initialized")
            
        schema_df = self.connection.execute("DESCRIBE netflix;").fetchdf()
        return schema_df.to_json(orient="records", indent=2)

    async def _get_sample_data(self) -> str:
        """Get sample data as a resource."""
        if not self.connection:
            raise RuntimeError("Database not initialized")
            
        sample_df = self.connection.execute("SELECT * FROM netflix LIMIT 5;").fetchdf()
        return sample_df.to_json(orient="records", indent=2)

    async def run(self):
        """Run the MCP server."""
        try:
            # Initialize components
            await self._initialize_database()
            await self._initialize_openai()
            
            # Run the server
            from mcp.server.stdio import stdio_server
            
            logger.info("Starting DuckDB MCP Server")
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="duckdb-mcp-server",
                        server_version="1.0.0",
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(),
                            experimental_capabilities={}
                        )
                    )
                )
                
        except Exception as e:
            logger.error(f"Server error: {e}")
            raise


async def main():
    """Main entry point."""
    server = DuckDBMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main())
