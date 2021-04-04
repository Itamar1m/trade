from .views import *
import requests
import json

def stock_name(ticker,api_key):

    api_result = requests.get(f'http://api.marketstack.com/v1/tickers/{ticker}?access_key={api_key}')

    name_data = api_result.json()

    return name_data



def high_low_dif(high,low,date,stock):
    difference= round((float(high)-float(low)),2)
    print(difference)
    perc =round(((difference/float(low))*100),2)
    print(perc)

    high_low_dif = InfoField.objects.get_or_create(name='Range')[0]
    field_data_h_l_dif=FieldData.objects.get_or_create(info =high_low_dif,amount = f'${difference}',date=date,stock=stock)[0]
    high_low_dif.field_datas.add(field_data_h_l_dif)

    high_low_perc = InfoField.objects.get_or_create(name= 'Range %')[0]
    field_data_h_l_perc = FieldData.objects.get_or_create(info =high_low_perc,amount= f'{perc}%',date = date,stock=stock)[0]
    high_low_perc.field_datas.add(field_data_h_l_perc)

    return field_data_h_l_dif , field_data_h_l_perc 




