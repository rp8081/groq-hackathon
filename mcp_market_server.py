from mcp.server.fastmcp import FastMCP
import yfinance as yf

mcp = FastMCP("market-data")

@mcp.tool()
def get_prices(ticker: str, period: str = "1mo", interval: str = "1d"):
    df = yf.download(ticker, period=period, interval=interval, progress=False, auto_adjust=True)
    if df is None or df.empty:
        return {"ticker": ticker, "prices": [], "note": "no data"}
    return {"ticker": ticker, "prices": df["Close"].tolist()}

if __name__ == "__main__":
    mcp.run_stdio()
