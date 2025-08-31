# MCP arXiv Server Docker Setup

This directory contains the Docker configuration for running the MCP arXiv server in a containerized environment.

## Files

- `Dockerfile` - Container definition for the MCP server
- `docker-compose.yml` - Docker Compose configuration for easy deployment
- `requirements.txt` - Python dependencies for the container
- `build-and-run.sh` - Helper script to build and run the container

## Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and run the container
docker-compose up --build

# Run in detached mode
docker-compose up -d --build

# Stop the container
docker-compose down
```

### Option 2: Using Docker directly (Standalone)

```bash
# Interactive mode (runs until you stop it)
./run-standalone.sh

# Or build and run manually
docker build -t mcp-arxiv-server .
docker run -it --rm -v $(pwd)/papers:/app/papers mcp-arxiv-server
```

### Option 3: Detached mode with helper scripts

```bash
# Start server in background
./start-detached.sh

# Interact with running server
./interact-detached.sh

# View logs
./logs-detached.sh

# Stop server
./stop-detached.sh
```

### Option 4: Direct MCP client connection

```bash
# Test connection and list all functionality
./mcp-docker-client.sh
```

## Helper Scripts

The following scripts are provided for easy container management:

- **`build-and-run.sh`** - Quick start with Docker Compose
- **`test-docker-setup.sh`** - Test the complete setup and list all MCP functionality
- **`run-standalone.sh`** - Run container without Docker Compose (interactive)
- **`start-detached.sh`** - Start container in background
- **`interact-detached.sh`** - Connect to running detached container
- **`logs-detached.sh`** - View logs from detached container
- **`stop-detached.sh`** - Stop and remove detached container
- **`mcp-docker-client.sh`** - Direct MCP client connection test

## Usage with MCP Clients

When using the containerized MCP server with clients like Claude Desktop, you'll need to modify your MCP client configuration to connect to the containerized server instead of running it directly.

### For Claude Desktop

Update your MCP settings to use the containerized server:

```json
{
  "servers": {
    "arxiv-research": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-arxiv-server", "python", "src/mcp_arxiv_server.py"],
      "transport": "stdio"
    }
  }
}
```

Or if using docker-compose:

```json
{
  "servers": {
    "arxiv-research": {
      "command": "docker-compose",
      "args": ["-f", "/path/to/your/mcp-arxiv/docker-compose.yml", "exec", "-T", "mcp-arxiv-server", "python", "src/mcp_arxiv_server.py"],
      "transport": "stdio"
    }
  }
}
```

## Data Persistence

The container is configured to persist paper data in the `./papers` directory on your host machine. This ensures that:

- Downloaded paper information persists between container restarts
- You can access the papers directly from your host system
- Data is not lost when the container is removed

## Environment Variables

You can customize the server behavior using environment variables:

- `PYTHONUNBUFFERED=1` - Ensures real-time output (already set)
- Add any additional configuration as needed

## Debugging

To debug issues with the containerized server:

```bash
# View logs
docker-compose logs -f mcp-arxiv-server

# Execute commands inside the running container
docker-compose exec mcp-arxiv-server bash

# Test the server directly
docker-compose exec mcp-arxiv-server python src/mcp_arxiv_server.py
```

## Stopping the Server

```bash
# Stop and remove containers
docker-compose down

# Stop and remove containers, networks, and volumes
docker-compose down -v
```
