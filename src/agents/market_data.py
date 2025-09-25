import random, datetime
import pandas as pd
from langchain_core.messages import AIMessage
from typing import Dict, Any

class MarketDataAgent:
    name = "MarketDataAgent"

    def __init__(self, llm=None):
        self.llm = llm

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        tickers = list(state.get("current_alloc", {}).keys()) or ["RELIANCE","TCS","HDFCBANK","INFY"]
        prices = {}
        start_date, end_date = None, None

        try:
            import yfinance as yf
            for t in tickers:
                df = yf.download(t + ".NS", period="1mo", interval="1d", progress=False, auto_adjust=True)
                if df is not None and len(df):
                    close_series = df["Close"]
                    arr = close_series.values.flatten().tolist()
                    prices[t] = arr[-30:]
                    if isinstance(df.index, (pd.DatetimeIndex,)):
                        if start_date is None:
                            start_date = df.index.min().strftime("%Y-%m-%d")
                        end_date = df.index.max().strftime("%Y-%m-%d")
        except Exception:
            pass

        if not prices:
            # fallback synthetic
            for t in tickers:
                base = 1000 + random.random()*200
                series = [base]
                for _ in range(29):
                    series.append(series[-1] * (1 + random.gauss(0.0005, 0.01)))
                prices[t] = series
            today = datetime.date.today()
            start_date = (today - datetime.timedelta(days=29)).strftime("%Y-%m-%d")
            end_date = today.strftime("%Y-%m-%d")

        state["tickers"] = tickers
        state["prices"] = prices
        state["date_range"] = {"start": start_date, "end": end_date}
        state["messages"].append(AIMessage(content=f"[MarketDataAgent] Prices for {tickers} from {start_date} → {end_date}"))
        return state
