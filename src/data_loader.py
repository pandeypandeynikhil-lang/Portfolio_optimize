import yfinance as yf
import pandas as pd

def get_data(tickers):
    data = yf.download(tickers, start="2020-01-01", auto_adjust=True)

    # Debug print (to verify structure)
    print("Columns:", data.columns)

    # If single stock, convert to DataFrame
    if isinstance(data, pd.Series):
        data = data.to_frame()

    returns = data.pct_change().dropna()
    return returns