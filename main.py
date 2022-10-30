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