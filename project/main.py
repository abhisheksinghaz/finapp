import yfinance as yf
import streamlit as st
import pandas as pd


# definig the ticker symbol
tickerSymbol = 'MSFT'
# try other tickerSymbols: AWS, AAPL, MSFT, 


st.write("""
# Simple Stock Price App

Shown are the stock details of 
""" + tickerSymbol)



# getting the data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31') # (period='max')

st.write("Closing price")
st.line_chart(tickerDf.Close)

st.write("Volume")
st.line_chart(tickerDf.Volume)

st.write("High")
st.line_chart(tickerDf.High)

st.write("Low")
st.line_chart(tickerDf.Low)