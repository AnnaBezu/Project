# Project
This is the shared repository used for project in Data Processing in Python course at the Institute of Economic Studies (IES) at Faculty of Social Sciences, Charles University. The **main goal** of this project is **stock market data analysis**. To be more precise, we will download historical stock data from Yahoo Finance and moreover, accounting and financial measures from Macrotrends using web scraping. Those will be used for financial and future value prediction analysis.

The **most important outcome** of this project for an outside viewer is probably the **web app** which combines all the aspects of our work - it includes data download, data display, graphical visualisation and stock´s future value prediction. Nevertheless, the web app provides just the outcomes and final outputs. In case you would like to see in detail what steps we took - how we work with data, what prediction techniques we use and how we apply them - or you would be interested in replicating our work, we include the *.ipynb* files with the code, comments and explanations. These files could be also handy if you are not able to launch the web app for some reason. If that is the case, you do not have to be disappointed. The files provided will lead you through what was consecutively supposed to happen, even though it might be less "smooth" than scrolling though the web app.  
 
  
 
**Description of the main parts:**


**Data download:**

Data download consists of two parts - Yahoo Finance and Macrotrends.net. We use Yahoo Finance to download stock market data on stocks from S&P 500 index. To get the ticker abbreviations of companies from S&P 500 and the industries they operate in, we webscrape Wikipedia. As regards Macrotrends, we use webscrapping to extract the following accounting and financial measures - Current Ratio, Long-term Debt/Capital, Debt/Equity ratio, Gross Margin, Operating Margin, EBIT Margin, EBITDA Margin, Pre-Tax Profit Margin, Net Profit Margin, Asset Turnover, Inventory Turnover Ratio, Receivable Turnover, Days Sales in Receivables, ROE, Return on Tangible Equity, ROA, ROI, Book Value Per Share, Operating Cash Flow Per Share, Free Cash Flow Per Share.


**Stock prediction:**

Assuming the viewer of this project is considering trading on stock market, the prediction models could be useful since they give its user an idea of how might the prices on the market develop and also help an individual to understand the market´s complexity. In our project, the prediction section will be divided into two parts depending on the prediction horizon - short-term predictions and long-term predictions. To model stocks´ short-term development (i.e. one-day ahead prediction), we will employ two techniques - standard averaging (STA) and exponential moving average (EMA). Predicting in long-term horizon will be covered by Long Short-Term Memory model. For more details, go to *predictions_sta_ema.ipynb* and *predictions_lstm.ipynb*, respectively. Short-term predicting is part of the web app, while long-term predicting is considered as "bonus" and is given only in the *.ipynb* file (*predictions_lstm.ipynb*).


**Web app:**

The web app combines all the parts done separately in the *.ipynb* files (web scrapping, data download, data visualisation, stock prediction) and displays it in user-friendly way. The user can specify stocks for which the analysis will be conducted. The data outputs are displayed in the form of interactive tables and graphs with the aim to provide user with little or no programming experience a way to easily perform basic analysis of stock market. 

The web app is build via streamlit. To be able to run it, you need to have the packages mentioned below installed. After typing *streamlit run app.py* in the command line, the web app will open in your browser. However beforehand, it is necessary to download *.py* and *.txt* files in this repository and put them into your directory. Otherwise the app will encounter error. 

**Wep app manual:** 

When the app is launched, it gathers all necessary data on S&P 500 companies the user might make use of. The process unfortunately takes some time (about 15 minutes) but on the bright side, this step enables to change the parameters of the analysis anytime without needing to reload the data all over again. Once the data gathering is finished, user can use the app without further delays. 

Firstly, he **chooses specific stock(s)** he would like to work with. For efficiency reasons, the number of stocks selected is limited to 4 at maximum. **After the stocks are specified, it is necessary to click on *Click for check* button.** The app checks whether the critera regarding the stock selection are satisfied and if it can proceed further. If some problem ocurred, the web app informs the user of it, otherwise it provides raw data and visualisation. As already mentioned, the graphs and tables are quite interactive - any time you move with your cursor over particular table or graph, you will see small icons in the top right corner (those are for full screen view or saving), also when you point at particular point on the plot line, you will be provided with corresponding exact value and date. Note, that any time you change the structure of stocks selected, you need to click on *Click for check* button again.

Next section of the app deals with **financial ratio analysis**. User can opt for ticker (either ticker he already denoted at the beginning or entirely different one) and specific ratio he would like to see. Moreover, description of the accounting and financial ratios is provided in the expander.

The last section of the web app covers **stock´s value prediction**. After clicking on *Click for short term predictions* button, the user will be presented with predictions for tickers seleted at the beginning of the web app. The predictions are given in two tables which is in line with two short-term prediction methods we applied - standard averaging (STA) and exponential moving average (EMA). 


**NOTE:** You need to have the following packages installed for the code to run smoothly:
* pandas
* pandas_datareader
* numpy
* yfinance
* prettytable
* keras
* sklearn
* matplotlib
* streamlit
* bs4
* json
* datetime
* urllib.request
* time
* datetime

