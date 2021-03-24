from django.shortcuts import render,redirect
from.models import *
import requests
import json
from .forms import *


def test(request):
    return render(request,'test.html')



def create_table(request):
    if request.method == 'GET':
        my_form = TableCreationForm()

        return render(request,'table_creation.html',{'form':my_form})

    if request.method == 'POST':
        form = TableCreationForm(request.POST)
      
        if form.is_valid():
            name = form.cleaned_data["table_name"]
            volume = form.cleaned_data["volume"]
            high = form.cleaned_data["high_of_day"]
            low = form.cleaned_data["low_of_day"]
            open_price = form.cleaned_data["open_price"]
            closing_price = form.cleaned_data['closing_price']

            option_list=[volume,high,low,open_price,closing_price]
            string_list=['Volume','High of day','Low of day','Open price','Closing price']

            table = UserCustomTable.objects.create(name=name,profile=request.user)
            for i in range(len(option_list)):
                if option_list[i] == True:
                    column = string_list[i]
                    field = InfoField.objects.get_or_create(name=column)[0]
                    table.infos.add(field)

            # table.infos.add(*form.cleaned_data['columns'])
            return redirect('view-table',table.pk)

        else:
            return render(request,'table_creation.html',context)


def view_table(request,pk):
    if request.method =='GET':
        form = RowAdditionForm()
        table = UserCustomTable.objects.get(pk=pk)
        print(table.field_datas.all())

        return render(request,'view_table.html',{'form':form,'table':table})

    if request.method == 'POST':
        form = RowAdditionForm(request.POST)
        
        if form.is_valid():
            date = form.cleaned_data['date']
            ticker = form.cleaned_data['ticker']   

            api_key ='aebf9561aa30efca56f5da349ed48d74'

            symbols = ticker.lower()
            date_from = date
            date_to = date

            api_result = requests.get(f'http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbols}&date_from={date_from}&date_to={date_to}')
            data = api_result.json()
            print (data)

            stock = Stock.objects.get_or_create(symbol = symbols,full_name = 'Stock_name')[0]
            date =DateObject.objects.get_or_create(date=date_from)[0]
            low = InfoField.objects.get_or_create(name = 'Low of day')[0]
            volume = InfoField.objects.get_or_create(name ='Volume')[0]
            high = InfoField.objects.get_or_create(name ='High of day')[0]
            opening_price = InfoField.objects.get_or_create(name ='Open price')[0]
            close = InfoField.objects.get_or_create(name ='Closing price')[0]
           
            field_data_low = FieldData.objects.get_or_create(info = low, amount = data['data'][0]['low'],date=date,stock=stock)[0]
            field_data_volume = FieldData.objects.get_or_create(info = volume, amount = data['data'][0]['volume'],date=date,stock=stock)[0]
            field_data_high = FieldData.objects.get_or_create(info = high, amount = data['data'][0]['high'],date=date,stock=stock)[0]
            field_data_close = FieldData.objects.get_or_create(info = close, amount = data['data'][0]['close'],date=date,stock=stock)[0]
            field_data_open_price = FieldData.objects.get_or_create(info = opening_price, amount = data['data'][0]['open'],date=date,stock=stock)[0]
           
            low.field_datas.add(field_data_low)
            volume.field_datas.add(field_data_volume)
            high.field_datas.add(field_data_high)
            opening_price.field_datas.add(field_data_open_price)
            close.field_datas.add(field_data_close)

            table = UserCustomTable.objects.get(pk=pk)
            user_custom_table_stocks=UserCustomTableStocks.objects.get_or_create(date=date,stock=stock,user_custom_table=table)

            table.stocks.add(stock)

            table.infos.add(low,volume,high,opening_price,close)
           
            table.field_datas.add(field_data_low,field_data_volume,field_data_high,field_data_close,field_data_open_price)

           
            return redirect('view-table',table.pk)

















