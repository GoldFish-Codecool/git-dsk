import yfinance as yf


ticker = yf.Ticker("AAPL")


historical_data = ticker.history()

print(historical_data.head())