import yfinance as yf
import numpy as np


def risk_score(ticker_symbol, period):
    """
    Calculates a risk score for a given stock based on its ticker symbol and history period.

    :param ticker_symbol: The stock's ticker symbol as a string.
    :param period: The period over which to calculate the risk score ('1mo', '3mo', '6mo', '1y', '2y', etc.).
    :return: A tuple containing the risk score as a float, its corresponding risk level as a string, and an associated color.
    """
    # Fetch historical stock data
    ticker = yf.Ticker(ticker_symbol)
    ticker_data = ticker.history(period=f"{period}y")

    # Calculate daily returns
    daily_returns = ticker_data["Close"].pct_change().dropna()

    # Calculate the standard deviation of daily returns (volatility)
    volatility = daily_returns.std()

    # Annualize the volatility to get the risk score
    risk_score = round(volatility * np.sqrt(252), 4)

    # Determine risk level and color
    if 0 <= risk_score <= 0.1:
        risk_level = "Very Low Risk"
        color = "green"
    elif 0.1 < risk_score <= 0.2:
        risk_level = "Low Risk"
        color = "lightgreen"
    elif 0.2 < risk_score <= 0.3:
        risk_level = "Moderate Risk"
        color = "yellow"
    elif 0.3 < risk_score <= 0.4:
        risk_level = "Moderately High Risk"
        color = "orange"
    elif 0.4 < risk_score <= 0.5:
        risk_level = "High Risk"
        color = "orangered"
    elif 0.5 < risk_score <= 0.6:
        risk_level = "Very High Risk"
        color = "red"
    else:
        risk_level = "Extreme Risk"
        color = "darkred"

    return risk_score, risk_level, color
