import streamlit as st
import pandas as pd
from tseopt import get_all_options_data
from persiantools.jdatetime import JalaliDate
days = int(input("days to maturity: "))
entire_option_market_data = get_all_options_data()
df = pd.DataFrame(entire_option_market_data)

df = df[df['days_to_maturity'] == days]
df = df[['ua_ticker', 'begin_date']]
df = df.drop_duplicates(subset=["ua_ticker"])
df['begin_date'] = pd.to_datetime(df['begin_date'], format='%Y%m%d')
df['begin_date'] = df['begin_date'].apply(
    lambda x: JalaliDate.to_jalali(x).strftime('%Y-%m-%d'))
df.reset_index(inplace=True, drop=True)
st.write(df)
