import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply() # This is needed to run the interactive python

"""
Make Sure:
1. The server is running before running this (client-sse) script
2. The server is configured to use SSE transport
3. The server is listening on port 8000 

To run the server:

uv run server.py
"""

async def main():
    # Connect to the server using SSE
    async with sse_client("http://localhost:8000/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream=read_stream)





