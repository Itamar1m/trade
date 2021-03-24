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
            name_list=['volume','high_of_day','low_of_day','open_price','closing_price']
            string_list=['Volume','High of day','Low of day','Open price','Closing price']

            table = UserCustomTable.objects.create(name=name,profile=request.user)
            for i in range(len(option_list)):
                if option_list[i] == True:
                    list_name = name_list[i]
                    column = string_list[i]
                    field = InfoField.objects.get_or_create(name=column,list_name=list_name)[0]
                    table.infos.add(field)

            # table.infos.add(*form.cleaned_data['columns'])
            return redirect('view-table',table.pk)

        else:
            return render(request,'table_creation.html',context)


def view_table(request,pk):
    if request.method =='GET':
        table = UserCustomTable.objects.get(pk=pk)
        # try:
        #     field_data = table.field_datas.all()
        # except:
        #     pass   
        form = RowAdditionForm()
        infos = table.infos.all()
        field_list = []
        l=['volume']
        
        for i in range(len(infos)):
            x=infos[i].list_name
            l.append(x)
        print(l)  

        #     attrs=dir(field_data[0])
        #     item_list=[]
        #     for item in attrs:
        #         if item in columns:
        #             item_list.append(str(item))

        #     field_list=[]        
        #     for field in field_data:
        #         for attr in dir(field):
        #             if attr in columns:
        #                 attr=getattr(field,attr)
        #                 field_list.append(attr)

        #     print(item_list)            
        # except:
        #     pass
        # if not field_list:
        #     field_list=''    

        context = {
        'table':table,
        'form':form,
        'l':l,
        'infos':infos,
        
        }
    

        return render(request,'view_table.html',context)



    if request.method == 'POST':
        form = RowAdditionForm(request.POST)
      
        if form.is_valid():
            date = form.cleaned_data['date']
            ticker = form.cleaned_data['ticker'].lower()     

            api_key ='aebf9561aa30efca56f5da349ed48d74'

            symbols = ticker
            date_from = date
            date_to = date

            api_result = requests.get(f'http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbols}&date_from={date_from}&date_to={date_to}')
            data = api_result.json()
            stock=Stock.objects.get_or_create(symbol=symbols)[0]
            field_data =FieldData.objects.get_or_create(stock=stock,open_price=data['data'][0]['open'],closing_price=data['data'][0]['close'],low_of_day= data['data'][0]['low'],volume=data['data'][0]['volume'],high_of_day= data['data'][0]['high'],datetime=date_from)[0]
            table = UserCustomTable.objects.get(pk=pk)
            table.field_datas.add(field_data)
            
           

            return redirect('view-table',table.pk)
   

















