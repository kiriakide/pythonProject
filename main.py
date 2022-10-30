
import streamlit as st
from panel.interact import interact
import hvplot.pandas

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

stocks = vds.stocks()
stocks.head()

symbols = list(stocks.symbol.unique())
st.write(symbols)

select = pn.widgets.Select(name='Select', options=symbols)

# create function
def create_plot(symbol):
    return stocks[stocks['symbol'] == symbol].hvplot('date', 'price')

# create interaction between widget and function
interact(create_plot, symbol=select)
