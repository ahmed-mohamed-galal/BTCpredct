import streamlit as st
import pandas as pd 
import numpy as np
import sklearn
import category_encoders
import joblib

st.title("Welcome to My BTC Predection for the nest day")
def get_input():
    open = st.number_input("Enter a number of Start price")

    low = st.number_input("Enter a number of Lowest price" )

    close = st.number_input("Enter a number of End price")

    volume = st.number_input("Enter a Total BTC Traded (Volume)")

    quote_asset_volume = st.number_input("Enter a 	Total USDT Traded")

    trades = st.number_input("Enter a number Number of Trades")

    taker_buy_base = st.number_input("Enter a number of BTC Bought via Market Buys (Taker Buy Volume)")

    taker_buy_quote = st.number_input("Enter a number of USDT Spent via Market Buys (Taker Buy Value)")

    year = st.slider("Enter Year", min_value=2025, max_value=2030)

    month = st.slider("Enter month", min_value=0, max_value=12)

    day = st.slider("Enter day", min_value=0, max_value=31)

    return pd.DataFrame(data=[[open , low , close ,volume , quote_asset_volume , trades ,taker_buy_base,taker_buy_quote, year , month ,day]],
        columns=[ 'open' , 'low' , 'close' ,'volume' , 'quote_asset_volume' , 'trades','taker_buy_base','taker_buy_quote', 'year' , 'month' ,'day'])

predct = get_input()

if st.button("🔮 Predict Next Day's BTC Close Price"):       
    pl = joblib.load('btc.h5')
    st.write(pl.predict(predct))
