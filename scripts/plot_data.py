import streamlit as st
import yfinance as yf
import altair as alt
import pandas as pd


def plot_data(ticker_symbol, period):
    """
    Plots the historical stock data for a given stock based on its ticker symbol and the period in years.

    :param ticker_symbol: The stock's ticker symbol as a string.
    :param period: The period over which to calculate the risk score ('1mo', '3mo', '6mo', '1y', '2y', etc.).
    """
    # Fetch historical stock data
    ticker = yf.Ticker(ticker_symbol)
    ticker_data = ticker.history(period=f"{period}y").reset_index()

    # Calculate Average
    ticker_data["Average"] = (ticker_data["High"] + ticker_data["Low"]) / 2

    # Create an interactive Altair chart
    chart = (
        alt.Chart(ticker_data)
        .mark_line()
        .encode(x="Date:T", y="Average:Q", tooltip=["Date:T", "Average:Q"])
        .properties(
            title=f'Daily Average Price of {ticker.info.get("longName", ticker_symbol)} Stock Over the Last {period} Years',
            width=800,
            height=400,
        )
        .interactive()
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)
