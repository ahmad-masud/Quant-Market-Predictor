import yfinance as yf
import numpy as np

def risk_score(ticker_symbol, period) -> float:
    """
    Calculates a risk score for a given stock based on its ticker symbol and history period.
    
    :param ticker_symbol: The stock's ticker symbol as a string.
    :param history_period: The period over which to calculate the risk score ('1mo', '3mo', '6mo', '1y', '2y', etc.).
    :return: The risk score as a float.
    """
    # Fetch historical stock data
    ticker = yf.Ticker(ticker_symbol)
    ticker_data = ticker.history(period=f'{period}y')
    
    # Calculate daily returns
    daily_returns = ticker_data['Close'].pct_change().dropna()
    
    # Calculate the standard deviation of daily returns (volatility)
    volatility = daily_returns.std()
    
    # Annualize the volatility to get the risk score
    # Assuming 252 trading days in a year
    risk_score = volatility * np.sqrt(252)

    # Print the risk score
    print(f'Risk Score for {ticker.info["longName"]}: {risk_score:.4f}')

    # Print the risk level based on the risk score
    if 0 <= risk_score <= 0.1:
        print("Risk Level: Very Low Risk")
    elif 0.1 < risk_score <= 0.2:
        print("Risk Level: Low Risk")
    elif 0.2 < risk_score <= 0.3:
        print("Risk Level: Moderate Risk")
    elif 0.3 < risk_score <= 0.4:
        print("Risk Level: Moderately High Risk")
    elif 0.4 < risk_score <= 0.5:
        print("Risk Level: High Risk")
    elif 0.5 < risk_score <= 0.6:
        print("Risk Level: Very High Risk")
    elif 0.6 < risk_score:
        print("Risk Level: Extreme Risk")
    
    # Return the risk score
    return round(risk_score, 4)
