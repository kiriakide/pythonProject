import streamlit as st

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealaaathCoach :heart: :running:")
    st.subheader("hey")

st.sidebar.success("select a page above")

import panel as pn
import streamlit as st
from panel.interact import interact
pn.extension()

import hvplot.pandas


stocks = vds.stocks()
stocks.head()
st.write(stocks)
st.print(stocks)

symbols = list(stocks.symbol.unique())
st.write(symbols)