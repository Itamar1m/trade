from .views import *
import requests
import json

def stock_name(ticker,api_key):

    api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}?{api_key}')

    name_data = api_result.json()

    return name_data

h=3

