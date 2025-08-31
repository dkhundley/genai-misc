from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio

async def connect_to_mcp_server():

    server_params = StdioServerParameters(
        command = "python",
        args = ["./mcp_arxiv_server.py"],
        env = None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()
            try:
                # Check if list_tools requires parameters, e.g.:
                # response = await session.list_tools(some_param)
                # List available prompts
                prompts = await session.list_prompts()
                print(f"Available prompts: {[p.name for p in prompts.prompts]}")

                # List available resources
                resources = await session.list_resources()
                print(f"Available resources: {[r.uri for r in resources.resources]}")

                # List available tools
                tools = await session.list_tools()
                print(f"Available tools: {[t.name for t in tools.tools]}")

            except Exception as e:
                print(f"Error calling list_tools: {e}")

if __name__ == '__main__':
    asyncio.run(connect_to_mcp_server())