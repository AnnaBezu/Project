import requests
import re
import json
from bs4 import BeautifulSoup as bs

def get_data_macro(stock_name):
    url = f'https://www.macrotrends.net/stocks/charts/{stock_name}/3m/financial-ratios?freq=Q'
    response = requests.get(url)
    p = re.compile(r' var originalData = (.*?);\r\n\r\n\r',re.DOTALL)
    data = json.loads(p.findall(response.text)[0])
    headers = list(data[0].keys())
    headers.remove('popup_icon')
    ratios = []
    for row in data:
        soup = bs(row['field_name'])
        field_name = soup.select_one('a, span').text
        fields = list(row.values())[2:]
        fields.insert(0, field_name)
        ratios.append(fields)
    pd.option_context('display.max_rows', None, 'display.max_columns', None)
    df = pd.DataFrame(ratios, columns = headers)
    return df
