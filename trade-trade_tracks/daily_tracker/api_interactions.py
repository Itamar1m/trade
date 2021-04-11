from .views import *
import requests
import json

def stock_name(ticker,api_key):

    api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}?access_key={api_key}')

    name_data = api_result.json()

    return name_data



def high_low_dif(high,low,date,stock):
    difference= round((float(high)-float(low)),2)
    perc =round(((difference/float(low))*100),2)
  
    high_low_dif = InfoField.objects.get_or_create(name='Range')[0]
    field_data_h_l_dif=FieldData.objects.get_or_create(info =high_low_dif,amount = f'${difference}',date=date,stock=stock)[0]
    high_low_dif.field_datas.add(field_data_h_l_dif)

    high_low_perc = InfoField.objects.get_or_create(name= 'Range %')[0]
    field_data_h_l_perc = FieldData.objects.get_or_create(info =high_low_perc,amount= f'{perc}%',date = date,stock=stock)[0]
    high_low_perc.field_datas.add(field_data_h_l_perc)

    return field_data_h_l_dif , field_data_h_l_perc 

api_key ='pp9Bo8dAXHWwaUcqYimJqf1x5doWrqED'

def pre_after(date,stock):
    date_api= date.date
    
    stock_api=stock.symbol.upper()

    response=requests.get(f'https://api.polygon.io/v1/open-close/{stock_api}/{date_api}?unadjusted=true&apiKey={api_key}')
    data =response.json()

    pm =data['preMarket'] 
    ah = data['afterHours']
    high_pre_market = InfoField.objects.get_or_create(name="Open-PM")[0]
    field_data_pm_high = FieldData.objects.get_or_create(info=high_pre_market,amount=f'${pm}',date=date,stock=stock)[0]
    high_pre_market.field_datas.add(field_data_pm_high)

    high_after_hours = InfoField.objects.get_or_create(name="Close-AH")[0]
    field_data_ah_high = FieldData.objects.get_or_create(info=high_after_hours,amount=f'${ah}',date=date,stock=stock)[0]
    high_after_hours.field_datas.add(field_data_ah_high)

    return field_data_pm_high , field_data_ah_high

def stock_info(stock,date):
  
    results=requests.get (f'https://api.polygon.io/v1/meta/symbols/{stock.symbol.upper()}/company?&apiKey={api_key}')
    data =results.json()

    industry = InfoField.objects.get_or_create(name="Industry")[0]
    field_data_industry = FieldData.objects.get_or_create(info=industry,amount=data['industry'],date=date,stock=stock)[0]
    industry.field_datas.add(field_data_industry)

    sector = InfoField.objects.get_or_create(name ='Sector')[0]
    field_data_sector = FieldData.objects.get_or_create(info= sector, amount = data['sector'],date=date,stock=stock)[0]
    sector.field_datas.add(field_data_sector)

    market_cap = InfoField.objects.get_or_create(name="Market cap")[0]
    field_data_market_cap = FieldData.objects.get_or_create(info=market_cap,amount= data['marketcap'],date=date,stock=stock)[0]
    market_cap.field_datas.add(field_data_market_cap)

    return field_data_market_cap,field_data_sector,field_data_industry

def open_close(date,stock,close,open_price):
    open_close_dif_am=round(float(float(close.amount)-float(open_price.amount)),2)
    open_close_dif_perc = round(((open_close_dif_am/float(open_price.amount))*100),2)

    open_close_dif = InfoField.objects.get_or_create(name='Open-Close-Dif')[0]
    field_data_ocd = FieldData.objects.get_or_create(info =open_close_dif,amount= f'${open_close_dif_am}',date=date,stock=stock)[0]
    open_close_dif.field_datas.add(field_data_ocd)

    open_close_perc = InfoField.objects.get_or_create(name='Open-Close%')[0]
    field_data_ocp = FieldData.objects.get_or_create(info =open_close_perc,amount=f'{open_close_dif_perc}%',date=date,stock=stock)[0]
    open_close_perc.field_datas.add(field_data_ocp)

    return field_data_ocp,field_data_ocd









    




