import sys, asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "mcp_market_server.py"],
        cwd="."
    )
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            res = await session.call_tool(
                "get_prices",
                {"ticker": "RELIANCE.NS", "period": "1mo", "interval": "1d"}
            )
            print(res)

if __name__ == "__main__":
    asyncio.run(main())
