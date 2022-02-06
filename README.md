# Project
This is the shared repository used for project in Data Processing in Python course at the Institute of Economic Studies (IES) at Faculty of Social Sciences, Charles University. The **main goal** of this project is **stock market data analysis**. To be more precise, we will download historical stock data from Yahoo Finance and moreover, accounting and financial measures from Macrotrends using web scraping. 

The **most important outcome** of this project for an outside viewer is probably the **web app** which combines all the aspects of our work - it includes data download, data display, graphical visualisation and stock´s future value prediction. Nevertheless, the web app provides just the outcomes and final outputs. In case you would like to see in detail what steps we took - how we work with data, what prediction techniques we use and how we apply them - or you would be interested in replicating our work, we include the ipynb files with the code, comments and explanations. These files could be also handy if you are not able to launch the web app for some reason. If that is the case, you do not have to be disappointed. The files provided will lead you through what was consecutively supposed to happen, even though it might be less "smooth" than scrolling though the web app.  
 
  
 
**Description of the main parts:**

**Data download:**

Data download consists of two parts - Yahoo Finance and Macrotrends.net. We use Yahoo Finance to download stock market data on stock from S&P 500 index. To get the ticker abbreviations of companies from S&P 500 and the industries they operate in, we webscrape Wikipedia. As regards Macrotrends, we use webscrapping to extract the following accounting and financial measures - Current Ratio, Long-term Debt/Capital, Debt/Equity ratio, Gross Margin, Operating Margin, EBIT Margin, EBITDA Margin, Pre-Tax Profit Margin, Net Profit Margin, Asset Turnover, Inventory Turnover Ratio, Receivable Turnover, Days Sales in Receivables, ROE, Return on Tangible Equity, ROA, ROI, Book Value Per Share, Operating Cash Flow Per Share, Free Cash Flow Per Share.

**Financial analysis:**

aa

**Stock prediction:**

Assuming the viewer of this project is considering trading on stock market, the prediction models could be useful since they give its user an idea of how might the prices on the market develop and also help an individual to understand the market´s complexity. In our project, the prediction section will be divided into two parts depending on the prediction horizon - short-term predictions and long-term predictions. To model stocks´ short-term development (i.e. one-day ahead prediction), we will employ two techniques - standard averaging (STA) and exponential moving average (EMA). Predicting in long-term horizon will be covered by Long Short-Term Memory model. For more details. go to *predictions_sta_ema.ipyng* and *predictions_lstm.ipyng*, respectively.

**Web app:**

The web app combines all the parts done separately in the ipynb files (web scrapping, data download, data visualisation, stock prediction) and displays it in user-friendly way. The user can specify stocks for which the analysis will be conducted. The data outputs are displayed in form of interactive tables and graphs with the aim to provide user with little or no programming experience a way to easily perform basic analysis of stock market. 

Wep app manual:


**NOTE:** You need to have the following packages installed for the code to run smoothly:
* pandas
* pandas_datareader
* numpy
* yfinance
* prettytable
* keras
* sklearn
* matplotlib
