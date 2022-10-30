import panel as pn
import streamlit as st
from panel.interact import interact
pn.extension()

import hvplot.pandas

import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

import geoviews as gv
gv.extension('bokeh')

from vega_datasets import data as vds
from pydataset import data as pyds

import yfinance

stocks = vds.stocks()
stocks.head()
st.write(stocks)
st.print(stocks)