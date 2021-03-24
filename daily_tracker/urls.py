from django.urls import path
from . import views

urlpatterns=[
    path('test/',views.test,name='test'),
    # path('get_data/<int:pk>',views.get_data,name='get-data'),
    # path('add_row/<int:pk>',views.add_row,name='add-row'),
    path('create_table/',views.create_table,name='create-table'),
    path('view_table/<int:pk>',views.view_table,name='view-table'),
    # path('get_data2/<int:pk>',views.get_data2,name='get-data2')
 ]


 # def get_data(request,pk):
#     if request.method =='GET':
#         form = RowAdditionForm()
#         return render(request,'view_table.html',{'form':form})

#     if request.method == 'POST':
#         form = RowAdditionForm(request.POST)
     
#         if form.is_valid():
#             date = form.cleaned_data['date']
#             ticker = form.cleaned_data['ticker']   

#             api_key ='aebf9561aa30efca56f5da349ed48d74'

#             symbols = ticker
#             date_from = date
#             date_to = date

#             api_result = requests.get(f'http://api.marketstack.com/v1/eod?access_key={api_key}&symbols={symbols}&date_from={date_from}&date_to={date_to}')
#             data = api_result.json()
#             print (data)

#             stock = Stock.objects.get_or_create(symbol = symbols,full_name = 'Stock_name')[0]
#             low = InfoField.objects.get_or_create(name = 'Low of day')[0]
#             volume = InfoField.objects.get_or_create(name ='Volume')[0]
#             field_data_low = FieldData.objects.create(name = low, amount = data['data'][0]['low'],datetime=date_from,stock=stock)
#             field_data_volume = FieldData.objects.create(name = volume, amount = data['data'][0]['volume'],datetime=date_from,stock=stock)
#             low.field.add(field_data_low)
#             volume.field.add(field_data_volume)
#             # add to particular table:
#             table = table.objects.get(pk=pk)
#             table.infos.add(low)
#             table.infos.add(volume)

#             return render(request,'test.html',{'response':data})

