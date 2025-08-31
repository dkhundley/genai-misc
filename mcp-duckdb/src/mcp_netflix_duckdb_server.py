import os
import json
import yaml
from typing import Any, Dict, List, Optional

import duckdb
import openai
import polars as pl

# Loading the OpenAI API key from file
with open('../../keys/api_keys.yaml') as f:
    api_keys = yaml.safe_load(f)

# Instantiating the OpenAI client
openai_client = openai.OpenAI(api_key = api_keys['OPENAI_API_KEY'])

# Loading the Netflix data from file
df_netflix = pl.read_csv('../data/netflix_data.csv')

# Loading the Netflix data into DuckDB
duckdb_connection = duckdb.connect()
duckdb_connection.register('netflix', df_netflix)