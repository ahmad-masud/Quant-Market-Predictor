import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

popular_ticker_symbols = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "GOOGL": "Alphabet Inc. (Google)",
    "FB": "Meta Platforms, Inc. (formerly Facebook, Inc.)",
    "BRK.A": "Berkshire Hathaway Inc.",
    "JNJ": "Johnson & Johnson",
    "V": "Visa Inc.",
    "WMT": "Walmart Inc.",
    "TSLA": "Tesla, Inc.",
}

print('''
  /$$$$$$  /$$      /$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$| $$__  $$
| $$  \ $$| $$$$  /$$$$| $$  \ $$
| $$  | $$| $$ $$/$$ $$| $$$$$$$/
| $$  | $$| $$  $$$| $$| $$____/ 
| $$/$$ $$| $$\  $ | $$| $$      
|  $$$$$$/| $$ \/  | $$| $$      
 \____ $$$|__/     |__/|__/      
      \__/                       
''')                                                                                                            
                                                                                                            

# Define the ticker symbol
print('Popular Ticker Symbols:\n')
for symbol, company in popular_ticker_symbols.items():
    print(f"{symbol} - {company}")

print('\nFind more ticker symbols at https://stockanalysis.com/stocks/\n')

# User inputs
ticker_symbol = input('Enter the ticker symbol: ')
period = input('How far back do you want data from, choose a period in years from 1 to 20: ')
x_days = int(input("Enter the number of days into the future for the prediction: "))

# Fetch historical stock data
ticker = yf.Ticker(ticker_symbol)
ticker_data = ticker.history(period=f'{period}y')

# Preparing the data
ticker_data['Target'] = ticker_data['Close'].shift(-x_days)
ticker_data = ticker_data.dropna()  # Dropping NA values to avoid issues in model training

# Features and Labels
X = ticker_data[['Close']]
y = ticker_data['Target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# MSE
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Predicting the future price based on the latest price
latest_price = np.array([[ticker_data['Close'].iloc[-1]]])  # Ensure latest_price is 2D

# Predicting a single future price
future_price = model.predict(latest_price)

print(f"Predicted stock price for {ticker_symbol} {x_days} days into the future: {future_price[0]:.2f}")

def plot_data():
    plt.figure(figsize=(14, 7))
    plt.plot(ticker_data.index, ticker_data['Average'], label='Daily Average Price', linewidth=1)

    plt.title(f'Daily Average Price of {ticker.info["longName"]} Stock Over the Last 10 Years')
    plt.xlabel('Date')
    plt.ylabel('Average Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()
