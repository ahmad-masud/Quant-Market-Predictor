import streamlit as st
import yfinance as yf
from scripts import predict_future_price, risk_score, plot_data

# Set the app title
st.title("Quant Market Predictor")

# Predefined list of popular ticker symbols
popular_tickers = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "GOOGL": "Alphabet Inc. (Google)",
    "FB": "Meta Platforms, Inc.",
    "BRK.A": "Berkshire Hathaway Inc.",
    "JNJ": "Johnson & Johnson",
    "V": "Visa Inc.",
    "WMT": "Walmart Inc.",
    "TSLA": "Tesla, Inc.",
}

# Create a dropdown to select ticker
ticker_symbol = st.selectbox("Select a stock ticker:", list(popular_tickers.keys()))
custom_ticker = st.text_input("Or enter a custom ticker symbol:")

# Use custom input if provided
ticker_symbol = custom_ticker.upper() if custom_ticker else ticker_symbol

# Select period for historical data
period = st.slider("Select historical period (years):", 1, 20, 5)

# Check if valid ticker
if not yf.Ticker(ticker_symbol).history(period="20y").empty:
    st.success(
        f"Analyzing {ticker_symbol} ({popular_tickers.get(ticker_symbol, 'Custom Stock')})"
    )

    option = st.radio(
        "Choose an analysis:",
        ["Predict Future Price", "Measure Stock Risk", "Plot Historical Data"],
    )

    if option == "Predict Future Price":
        x_days = st.number_input(
            "Enter the number of days into the future:",
            min_value=1,
            max_value=365,
            value=30,
        )
        if st.button("Predict Price"):
            predicted_price = predict_future_price(ticker_symbol, x_days, period)
            st.write(
                f"Predicted price for {ticker_symbol} in {x_days} days: **${predicted_price}**"
            )

    elif option == "Measure Stock Risk":
        if st.button("Calculate Risk Score"):
            risk_score, risk_level, color = risk_score(ticker_symbol, period)
            st.write(f"Risk Score for {ticker_symbol}: **{risk_score}**")
            st.write(
                f'<span style="color: {color};">{risk_level}</span>',
                unsafe_allow_html=True,
            )

    elif option == "Plot Historical Data":
        if st.button("Show Chart"):
            plot_data(ticker_symbol, period)
else:
    st.error("Invalid ticker symbol. Please enter a valid stock ticker.")
