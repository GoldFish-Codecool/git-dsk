import yfinance as yf


ticker = yf.Ticker("AAPL")


historical_data = ticker.history(interval="1d")

print(historical_data.head())