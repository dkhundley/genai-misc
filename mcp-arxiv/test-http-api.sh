#!/bin/bash

# Test script for MCP arXiv HTTP API using proper JSON-RPC over HTTP

echo "🧪 Testing MCP arXiv HTTP API (JSON-RPC over Streamable HTTP)..."
echo "=============================================================="

# Start the HTTP server
echo "🚀 Starting HTTP MCP server..."
docker-compose up -d mcp-arxiv-http

# Wait for the server to start
echo "⏳ Waiting for server to start..."
sleep 5

# Base URL
BASE_URL="http://localhost:8000/mcp"

echo ""
echo "🔍 Running MCP JSON-RPC tests..."
echo ""

# Test 1: Initialize MCP session
echo "1. Initialize MCP Session:"
INIT_RESPONSE=$(curl -i -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {"name": "curl-test", "version": "1.0"}
    }
  }')

echo "Response Headers:"
echo "$INIT_RESPONSE" | sed -n '1,20p'
echo ""

# Extract session ID if present
SID=$(echo "$INIT_RESPONSE" | awk -F': ' '/^mcp-session-id:/{print $2}' | tr -d '\r\n ')
echo "Session ID: ${SID:-'Not provided'}"
echo ""

# Set up headers for subsequent requests
if [ -n "$SID" ]; then
    SESSION_HEADER="-H mcp-session-id:$SID"
else
    SESSION_HEADER=""
fi

# Send initialized notification (required by MCP protocol)
echo "Sending initialized notification..."
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{"jsonrpc": "2.0","method": "notifications/initialized"}' > /dev/null

echo "Initialization complete!"
echo ""

echo "---"
echo ""

# Test 2: List prompts
echo "2. List Prompts:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "prompts/list"
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

# Test 3: List tools
echo "3. List Tools:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/list"
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

# Test 4: List resources
echo "4. List Resources:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "resources/list"
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

# Test 5: Call search_papers tool
echo "5. Call search_papers tool:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
      "name": "search_papers",
      "arguments": {
        "topic": "machine learning",
        "max_results": 3
      }
    }
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

# Test 6: Get a prompt
echo "6. Get generate_search_prompt:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 6,
    "method": "prompts/get",
    "params": {
      "name": "generate_search_prompt",
      "arguments": {
        "topic": "artificial intelligence",
        "num_papers": 5
      }
    }
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

# Test 7: Read a resource
echo "7. Read papers://folders resource:"
curl -sS -X POST "$BASE_URL" \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  $SESSION_HEADER \
  -d '{
    "jsonrpc": "2.0",
    "id": 7,
    "method": "resources/read",
    "params": {
      "uri": "papers://folders"
    }
  }' | grep '^data: ' | sed 's/^data: //' | python3 -m json.tool
echo ""

echo "✅ All HTTP MCP tests completed!"
echo ""
echo "📊 Server Status:"
docker-compose ps mcp-arxiv-http
echo ""
echo "🌐 MCP Endpoint: http://localhost:8000/mcp"
echo "📋 Protocol: JSON-RPC 2.0 over Streamable HTTP"
echo ""
echo "To stop the server: docker-compose down"
