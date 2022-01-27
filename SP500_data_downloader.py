import pandas as pd
import numpy as np
import requests
import bs4 as bs
from datetime import date
import urllib.request
import time
from bs4 import BeautifulSoup
import streamlit
import matplotlib.pyplot as plt
import yfinance as yf

#Get stock names S&P 500 from Wikipedia
def SP500():
    req = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(req.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    #prepare variables 
    tickers=[]
    sector = []
    for row in table.findAll('tr')[1:]:
        tic = row.findAll('td')[0].text
        #sector
        sec = row.findAll('td')[4].text
        tickers.append(tic)
        sector.append(sec)
    tickers = list(map(lambda s: s.strip(), tickers))
    industries = list(map(lambda s: s.strip(), sector))
    tickerdf = pd.DataFrame(tickers,columns=['ticker'])
    sectordf = pd.DataFrame(industries,columns=['industry'])
    df = pd.concat([tickerdf, sectordf], axis=1)
    df2 = df.reindex(tickerdf.index)
    #ALL TICKERS FROM S&P
    tick = df['ticker'].to_numpy()
    tick_to_download = tick.tolist()
    return tick_to_download

def get_data():
    tick_to_download = SP500()
    #set the beginning of time series to 1st of Jan 2010
    BEGINNING = "2010-01-01"
    #Set today's date
    TODAY = date.today().strftime("%Y-%m-%d")
    #DOWNLOADING DATA
    data = yf.download(tick_to_download,start=BEGINNING,end=TODAY)
    data = data.reset_index()
    df = pd.DataFrame(data=data)
    df
    return df