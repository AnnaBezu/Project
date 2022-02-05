import numpy as np
import yfinance as yf
import pandas as pd
#!pip install prettytable
from prettytable import PrettyTable #for table
import SP500_data_downloader as SP
from SP500_data_downloader import *

# create the dataset consisting only from 9 tickers
aa=get_data_try()


#defining a function for rounding to specific number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


# define the list of tickers
ticker_list=["MSFT", "GE", "AA"]

# define the function for STA predictions
def pred_sta(ticker_list):
    # specify the column names while initializing the table 
    myTable = PrettyTable(["Ticker", "Prediction method", "Open", "Close", "Volume"]) 

    for ticker in ticker_list:
        data_volume=aa.Volume[ticker_list][ticker]
        data_close=aa.Close[ticker_list][ticker]
        data_open=aa.Open[ticker_list][ticker]
        N = 100 #from how many prices back is the average computed

        std_prediction_list=[1,2,3] #create a list to which we will write the prediction values (it cannot be empty because with lists, we can 
                             # use indexing only to access or modify an item that already exists ) 
        pred_idex=-1

        Open=data_open
        Close=data_close
        Volume=data_volume

        featurelist = [Open, Close, Volume]
        for feature in featurelist:
            pred_idex=pred_idex+1
            feature[feature.size - N:, ]
            std_prediction = truncate(np.mean(feature[feature.size - N:, ]),2)
            std_prediction_list[pred_idex]=std_prediction #assign predicted value to a specific position in std_predictions_list

        
        print("Short-term predictions on ticker", ticker, "are:")
        print(std_prediction_list)
        print("")
        myTable.add_row([ticker, "Standard Averaging", std_prediction_list[0], std_prediction_list[1], std_prediction_list[2]]) 
    print("")
    print("")
    print("Or summarized in the table for better comparison:")
    print(myTable)
    std_table=myTable 
    
    
# define the function for EMA predictions
def pred_ema(ticker_list):
    # specify the column names while initializing the table 
    myTable = PrettyTable(["Ticker", "Prediction method", "Open", "Close", "Volume"]) 


    for ticker in ticker_list:
        siz=len(aa)
        idex=0
        running_mean = 0.0
        gamma=0.1

        exp_prediction_list=[1,2,3] #create a list to which we will write the prediction values (it cannot be empty because with lists, we can 
                             # use indexing only to access or modify an item that already exists ) 
        pred_idex=-1
    
        data_volume=aa.Volume[ticker_list][ticker]
        data_close=aa.Close[ticker_list][ticker]
        data_open=aa.Open[ticker_list][ticker]

        Open=data_open
        Close=data_close
        Volume=data_volume

        featurelist = [Open, Close, Volume]
        for feature in featurelist:
            running_mean = 0.0
            idex=0
            pred_idex=pred_idex+1
            while idex < siz:
            #calculation
                running_mean = running_mean*gamma + (1.0-gamma)*feature[idex]
                idex=idex+1
                exp_prediction=truncate(running_mean,2)
        
            exp_prediction_list[pred_idex]=exp_prediction #assign predicted value to a specific position in exp_predictions_list
    
            #print(exp_prediction)
        print("Short-term EMA predictions on ticker", ticker, "are:")
        print(exp_prediction_list)
        print("")
        myTable.add_row([ticker, "Exponential Moving Average", exp_prediction_list[0], exp_prediction_list[1], exp_prediction_list[2]]) 
    print("")
    print("")
    print("Or summarized in the table for better comparison:")
    print(myTable)
    exp_table=myTable    
    

