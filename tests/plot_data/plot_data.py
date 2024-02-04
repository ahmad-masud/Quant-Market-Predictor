import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(ticker_symbol, period):
    ticker = yf.Ticker(ticker_symbol)
    ticker_data = ticker.history(period=f'{period}y')

    ticker_data['Average'] = (ticker_data['High'] + ticker_data['Low']) / 2

    plt.figure(figsize=(14, 7))
    plt.plot(ticker_data.index, ticker_data['Average'], label='Daily Average Price', linewidth=1)

    plt.title(f'Daily Average Price of {ticker.info["longName"]} Stock Over the Last {period} Years')
    plt.xlabel('Date')
    plt.ylabel('Average Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

    return True;