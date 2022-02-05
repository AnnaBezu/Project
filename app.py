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

st.markdown("<h1 style='text-align: center; color: #6aa84f; '> STOCK PREDICTION </h1>", unsafe_allow_html=True)

st.markdown("""
Dear user,
data are uploading and it may take a while... This process may take approximately 15 minutes. Thanks to data upload at the beginning, you can further change your analysis without any further waiting.
""")

st.markdown("<h6 style='text-align: cleft; color: #6aa84f; '> Selection of data for analysis </h6>", unsafe_allow_html=True)

tickers=SP500()
data=get_data_try() #loading only 9 tickers


#@st.cache #LOADING ALL TICKERS
#def load_data():
#    data = get_data_yahoo()
#    return data

#data=load_data()

BEGINNING = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

selected_tickers = st.multiselect('Companies', tickers)  #selecting tickers for analysis

## Date slider
date1 = st.select_slider(
     'Select a final year of your analysis (format: Year-Month-Day)',
     options=['2016-12-31', '2017-12-31', '2018-12-31', '2019-12-31', '2020-12-31', '2021-12-31'])
st.write('Final date:', date1)

#Date from calendar
col1_date_initial, col2_date_final = st.columns(2)
col1_date_initial.write(' ## **Initial Date**')
date_initial = col1_date_initial.date_input('Select the first day for analysis')
col2_date_final.write('## **Final Date**')
date_final = col2_date_final.date_input('Select the final day of analysis')

data_volume=pd.DataFrame(data.Volume[selected_tickers],columns=selected_tickers)
data_volume.index = pd.to_datetime(data_volume.index)

data_close=pd.DataFrame(data.Close[selected_tickers],columns=selected_tickers)
data_close.index = pd.to_datetime(data_close.index)

data_open=pd.DataFrame(data.Open[selected_tickers],columns=selected_tickers)
data_open.index = pd.to_datetime(data_open.index)

#data['Date'] = pd.to_datetime(data['Date'],format='%Y%m%d')
#data['Date']=data['Date'].dt.date
#data['Date']=data['Date'].dt.date
#data.index=data.index.to_pydatetime()
#data_date=data.Date

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

    
if st.button('Click for data and graphs'):
        #Data and graph for close prise
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Close price of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data for close price for selected stocks. 
     """)

        col_close_t.subheader("Close price for selected stocks")
        col_close_t.write(data_close)
        
        #Data and graph for open price
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Open price of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data for open price for selected stocks. 
     """)

        col_close_t.subheader("Open price for selected stocks")
        col_close_t.write(data_close)
        
        #Data and graph for volume
        col_close, col_close_t = st.columns([3, 2])

        col_close.subheader("Volume of the stocks")
        col_close.line_chart(data_close)
        with st.expander("See explanation"):
                 st.write("""
         The chart and the table above show the data of volume for selected stocks. 
     """)

        col_close_t.subheader("Volume for selected stocks")
        col_close_t.write(data_close)

#def macro_df():
#    ratios=[]
#    for ticker in selected_tickers:
#        rat=get_data_macro(ticker)
#        ratios=pd.DataFrame(rat)
#        ratios=ratios.transpose() #IS IT RIGHT?
#        ratios.insert(1,'TICKER','')
#        ratios["TICKER"] = ticker
#        ratios[0,2]=''
#        ratios.rename(columns={'field_name':'Ratio'}, inplace=True)
#        return ratios

def macro_df():
    ratios=[]
    for ticker in selected_tickers:
        rat=get_data_macro(ticker)
        rat=rat.set_index('field_name').T
        ratios=pd.DataFrame(rat)
        ratios.insert(0,'TICKER','')
        ratios["TICKER"] = ticker
        #ratios.rename(columns={'field_name':'Ratio'}, inplace=True)
        return ratios
    
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
        ratio_selected=st.selectbox(
            'What ratio are you interested to display?',
            (list_of_ratios))
        with st.expander("See definitions of ratios"):
            with open('Ratios_def.txt') as f:
                for line in f:
                    st.write(line)
        st.subheader(f'Data for ratio: {ratio_selected}')
        df_ratio_selected=MT_data_show[ratio_selected]
        col_rat, col_rat_t = st.columns([3, 2])
        col_rat.subheader("Graph")
        col_rat.line_chart(df_ratio_selected)
        col_rat_t.subheader("Table")
        col_rat_t.write(df_ratio_selected)
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
