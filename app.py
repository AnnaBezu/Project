import streamlit
import yfinance
import plotly
import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
import SP500_data_downloader as SP
from SP500_data_downloader import *
import Macrotrends_downloader as MT
from Macrotrends_downloader import *
from IPython.display import clear_output
from pandas_datareader import DataReader
from streamlit.errors import StreamlitAPIException
import predictions_STA_EMA as STA_EMA
from predictions_STA_EMA import *


st.markdown("<h1 style='text-align: center; color: #6aa84f; '> STOCK PREDICTION </h1>", unsafe_allow_html=True)

st.markdown("""
Dear user,
data are uploading and it may take a while... This process may take approximately 15 minutes. Thanks to data upload at the beginning, you can further change your analysis without any additional waiting.
""")

st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> Selection of data for analysis </h6>", unsafe_allow_html=True)

tickers=SP500()

#LOADING ONLY 9 TICKERS
#@st.cache #LOADING ONLY 9 TICKERS
#def load_data():
#    data = get_data_try()
#    return data



#LOADING ALL TICKERS
@st.cache #LOADING ALL TICKERS
def load_data():
    data = get_data_yahoo()
    return data

data=load_data()


BEGINNING = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.write("Firstly, select a maximum of 4 shares.")

try:
    selected_tickers = st.multiselect('Companies', tickers)  #selecting tickers for analysis
#Dataframes
    data_volume=pd.DataFrame(data.Volume[selected_tickers],columns=selected_tickers)
    data_volume.index = pd.to_datetime(data_volume.index)

    data_close=pd.DataFrame(data.Close[selected_tickers],columns=selected_tickers)
    data_close.index = pd.to_datetime(data_close.index)

    data_open=pd.DataFrame(data.Open[selected_tickers],columns=selected_tickers)
    data_open.index = pd.to_datetime(data_open.index)
except KeyError:
     st.error('We are so sorry, you selected ticker, for which data are invalid. Please, select other ticker.')
    



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

st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> If you obrain a positive message, that analysis will work properly, you can proceed the analysis.  </h6>", unsafe_allow_html=True)

st.subheader('Financial data from Yahoo Finance')

if st.button('Click for data and graphs'):
        #Data and graph for close prise
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Close price of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data for close price for selected stocks. Closing price denotes the price at the end of the trading day at which security was transacted. As it is not influenced by stock splits or cash/stock dividens, it is a feature investors look at the most often.
     """)

        col_close_t.subheader("Close price for selected stocks")
        col_close_t.write(data_close)
        
        #Data and graph for open price
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Open price of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data for open price for selected stocks. Opening price refers to the price at which each stock is traded immediately after the stock exchange opens to trading. However, it is not the same as the closing price from previous trading day.
     """)

        col_close_t.subheader("Open price for selected stocks")
        col_close_t.write(data_close)
        
        #Data and graph for volume
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Volume of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data of volume for selected stocks. In general, trading volume measures how much certain financial asset is traded during specific period. In case of stocks, it means number of shares traded. Trading volumes are associated with market strength and thus, investors consider observing volume patterns very useful.
     """)

        col_close_t.subheader("Volume for selected stocks")
        col_close_t.write(data_close)

def macro_df():
    ratios=pd.DataFrame()
    for ticker in selected_tickers:
        rat=get_data_macro(ticker)
        rat=rat.set_index('field_name').T
        ratios2=pd.DataFrame(rat)
        ratios2.insert(0,'TICKER','')
        ratios2["TICKER"] = ticker
        ratios=ratios.append(ratios2)
        #ratios.rename(columns={'field_name':'Ratio'}, inplace=True)
    return(ratios) 
    
#Ratios for selected tickers
MT_data=macro_df()
MT_data=pd.DataFrame(MT_data)
MT_data_show = MT_data.astype(str)
list_of_ratios_with_T=MT_data_show.columns.to_list()
list_of_ratios=list_of_ratios_with_T[1:]
#list_of_ratios=MT_data_show["Ratio"].values.tolist()

st.subheader('Ratios from Macrotrends')
try:
    what_ratio = st.radio(
        "For what tickers do you want to see ratio?",
        ('For all selected tickers', 'For one from selected tickers', 'For one from all tickers from S&P 500'))
    if what_ratio == 'For all selected tickers':
        st.write('Here you can see ratios for all selected tickers')
        st.write(MT_data_show)
    elif what_ratio=='For one from selected tickers':
        st.write('Please, select one ticker from previously selected tickers.')
        option = st.selectbox(
             'Select to show ratios only for',
                (selected_tickers))
        st.write('You selected:', option)
        rat1=MT_data_show[MT_data_show["TICKER"] ==option]
        rat2=rat1.astype(str)
        st.write(rat2)
        ratio_selected2=st.selectbox(
        'What ratio are you interested to display?',
         (list_of_ratios))
        with st.expander("See definitions of ratios"):
            with open('Ratios_def.txt') as f:
                for line in f:
                    st.write(line)
        st.subheader(f'Data for ratio: {ratio_selected2}')
        df_rat_sel2=rat2[ratio_selected2]
        col_rat2, col_rat2_t = st.columns([4, 2])
        col_rat2.subheader("Graph")
        col_rat2.line_chart(df_rat_sel2)
        col_rat2_t.subheader("Table")
        col_rat2_t.write(df_rat_sel2)
    else:
        st.write('Please, select one ticker from S&P Tickers.')
        option2 = st.selectbox(
            'Select to show ratios only for',
            (tickers))
        st.write('You selected:', option2)
        rat3=get_data_macro(option2)
        rat3=rat3.set_index('field_name').T
        rat4=pd.DataFrame(rat3)
        rat4=rat4.astype(str)
        st.dataframe(rat4)
        ratio_selected3=st.selectbox(
         'What ratio are you interested to display?',
         (list_of_ratios))
        with st.expander("See definitions of ratios"):
            with open('Ratios_def.txt') as f:
                for line in f:
                    st.write(line)
        st.subheader(f'Data for ratio: {ratio_selected3}')
        df_rat_sel3=rat4[ratio_selected3]
        col_rat3, col_rat3_t = st.columns([4, 2])
        col_rat3.subheader("Graph")
        col_rat3.line_chart(df_rat_sel3)
        col_rat3_t.subheader("Table")
        col_rat3_t.write(df_rat_sel3)
except StreamlitAPIException:
    st.error('We are so sorry, you selected ticker, for which data are invalid. Please, select other ticker.')
    
st.subheader('Stock price and volume predictions')

if st.button('Click for short term predictions'):
    bb=pd.DataFrame(data)
    #st.write(",".join((selected_tickers)))
    st.write("In the tables below, you are given short-term (one trading day ahead) predictions on Open price, Close price and Volume of selected ticker(s).") 
    st.write("The first table contains predictions obtained via Standard Averaging (STA). The key idea of this method is to use historical values within specific time window (in this prediction we use 100 days), average them and use the obtained value as prediction for the following day.")
    st.write(pred_sta_app(selected_tickers, bb))
    st.write(" ")
    st.write(" ")
    st.write("The second table presents predictions coming from exponential averaging following Exponential Moving Average (EMA) methodology.")
    st.write(pred_ema_app(selected_tickers,bb))
    st.write(" ")
    st.write(" ")
    #st.write(data_volume)
    #st.write(" ")
    #st.write(" ")
    #st.write(pd.DataFrame(data.Volume[selected_tickers]["GE"],columns=selected_tickers))
    #st.write(" ")
    #st.write(" ")
    #st.write(pd.DataFrame(data.Close))
    #st.write(data)

st.subheader('Downloading data')

st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> If you would like to create your own analysis, you can download data for S&P 500 market index from Yahoo Finance below.  </h6>", unsafe_allow_html=True)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

data_csv = convert_df(data)

st.download_button(
     label="Download financial data",
     data=data_csv,
     file_name='data.csv',
     mime='text/csv',
 )
