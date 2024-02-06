import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def predict_future_price(ticker_symbol, x_days, period) -> float:
    """
    Predicts the future stock price for a given stock based on its ticker symbol and the number of days into the future.
    
    :param ticker_symbol: The stock's ticker symbol as a string.
    :param x_days: The number of days into the future for the prediction as an integer.
    :param period: The period over which to calculate the risk score ('1mo', '3mo', '6mo', '1y', '2y', etc.).
    :return: The predicted future stock price as a float.
    """
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
    print(f'Mean Squared Error: {mse}')

    # Predicting the future price based on the latest price
    # Ensure the input for prediction matches the training data format
    latest_price_df = pd.DataFrame({'Close': [ticker_data['Close'].iloc[-1]]})

    # Predicting a single future price using DataFrame to match training format
    future_price = model.predict(latest_price_df)

    # Print the predicted future price
    print(f'Predicted stock price for {ticker.info["longName"]} {x_days} days into the future: {future_price[0]:.2f}')

    return round(future_price[0], 2)
