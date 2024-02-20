import yfinance as yf
import matplotlib.pyplot as plt

def plot_data(ticker_symbol, period) -> bool:
    """
    Plots the historical stock data for a given stock based on its ticker symbol and the period in years.
    
    :param ticker_symbol: The stock's ticker symbol as a string.
    :param period: The period over which to calculate the risk score ('1mo', '3mo', '6mo', '1y', '2y', etc.).
    :return: True if the plot is successful, False otherwise.
    """
    # Fetch historical stock data
    ticker = yf.Ticker(ticker_symbol)
    ticker_data = ticker.history(period=f'{period}y')

    # Calculate Average
    ticker_data['Average'] = (ticker_data['High'] + ticker_data['Low']) / 2

    # Plot the historical stock data
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