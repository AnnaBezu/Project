import streamlit
import yfinance
import plotly
import ipywidgets as widgets
import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
import SP500_data_downloader as SP
from SP500_data_downloader import *
from IPython.display import clear_output
from pandas_datareader import DataReader

st.markdown("<h1 style='text-align: center; color: #6aa84f; '> STOCK PREDICTION </h1>", unsafe_allow_html=True)

st.markdown("""
Dear user,
data are uploading and it may take a while... This process may take approximately 15 minutes. Thanks to data upload at the beginning, you can further change your analysis without any further waiting.
""")

st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> Selection of data for analysis </h6>", unsafe_allow_html=True)

tickers=SP500()
data=get_data_try() #CHANGE THIS FUNCTION TO get_data_yahoo() TO GET ALL DATA!
with st.spinner('Data loading'):
    time.sleep(5)
st.success('Data are loaded!')

#data=get_data() #NOT USE - TAKES A LONG LONG LONG TIME

BEGINNING = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

selected_tickers = st.multiselect('Companies', tickers)  #selecting tickers for analysis

## Date
date1 = st.select_slider(
     'Select a final year of your analysis (format: Year-Month-Day)',
     options=['2016-12-31', '2017-12-31', '2018-12-31', '2019-12-31', '2020-12-31', '2021-12-31'])
st.write('Final date:', date1)

#Delete?
col1_date_initial, col2_date_final = st.columns(2)
col1_date_initial.write(' ## **Initial Date**')
date_initial = col1_date_initial.date_input('Select the first day for analysis')
col2_date_final.write('## **Final Date**')
date_final = col2_date_final.date_input('Select the final day of analysis')

#@st.cache(allow_output_mutation=True)
#def get_stock_data(ticker):
#    BEGINNING = "2019-01-01"
#    TODAY = date.today().strftime("%Y-%m-%d")
#    time.sleep(2)
#    data = yf.download(ticker,start=BEGINNING,end=TODAY)
#    return data

#tickerData = yf.Ticker('MSFT')
#tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2022-1-25')

data_volume=pd.DataFrame(data.Volume[selected_tickers],columns=selected_tickers)
data_close=pd.DataFrame(data.Close[selected_tickers],columns=selected_tickers)
data_open=pd.DataFrame(data.Open[selected_tickers],columns=selected_tickers)
#data['Date'] = pd.to_datetime(data['Date'],format='%Y%m%d')
#data['Date']=data['Date'].dt.date
#data['Date']=data['Date'].dt.date
#data.index=data.index.to_pydatetime()
#data_date=data.Date



 
type=data.columns
st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> Please, press the button to see if the analysis will continue to work correctly with the selected data.  </h6>", unsafe_allow_html=True)

if st.button('Click for check'):
    if len(selected_tickers) > 4:
        st.warning('You can select maximum 4 tickers for analysis. Please, reselect your tickers otherwise, the analysis may not be correct and some error may occur.')
    elif len(selected_tickers) <1:
        st.error('You must select at least 1 ticker.')
    else:
        st.write('With selected data, the analysis will work properly :-)')
        st.write("Your selected tickers are:")
        st.write(', '.join(selected_tickers))
        
        st.markdown('** Close price**.')
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Close price of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data for close price for selected stocks. 
     """)

        col_close_t.subheader("A narrow column with the data")
        col_close_t.write(data_close)
        
