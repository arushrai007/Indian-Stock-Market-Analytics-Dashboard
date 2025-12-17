import yfinance as yf
import pandas as pd

symbols = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS",
    "ICICIBANK.NS","SBIN.NS","ITC.NS","LT.NS",
    "AXISBANK.NS","KOTAKBANK.NS"
]

data = yf.download(symbols, start="2022-01-01", end="2025-01-01", group_by="ticker")

records = []

for stock in symbols:
    df = data[stock].reset_index()
    df["Stock"] = stock
    records.append(df)

final_df = pd.concat(records)
final_df.to_csv("indian_stock_market.csv", index=False)
