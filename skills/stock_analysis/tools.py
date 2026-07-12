import yfinance as yf
import json
from datetime import datetime
from langchain_core.tools import tool


@tool
def collect_yfinance_data(ticker: str) -> str:
    """
    Collect real-time financial data and indicators for a stock using Yahoo Finance.
    The ticker format must follow the Yahoo standard (e.g. 'PETR4.SA' for Petrobras or 'AAPL' for Apple).
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        regular_market_time = info.get("regularMarketTime")
        market_time = datetime.fromtimestamp(regular_market_time).isoformat() if regular_market_time else None

        filtered_data = {
            "ticker": ticker,
            "name": info.get("longName", "N/A"),
            "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "previous_close": info.get("previousClose"),
            "fifty_day_average": info.get("fiftyDayAverage"),
            "current_volume": info.get("volume"),
            "average_volume": info.get("averageVolume"),
            "currency": info.get("currency", "BRL"),
            "market_time": market_time
        }

        if filtered_data["current_price"] and filtered_data["previous_close"]:
            change = ((filtered_data["current_price"] - filtered_data["previous_close"]) / filtered_data["previous_close"]) * 100
            filtered_data["day_change"] = round(change, 2)
        else:
            filtered_data["day_change"] = 0.0

        return json.dumps(filtered_data, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"error": f"Could not collect data for ticker {ticker}. Reason: {str(e)}"})
