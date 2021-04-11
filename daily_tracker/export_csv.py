from .views import *
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
import csv

def export_csv(request,pk):
    table= UserCustomTable.objects.get(pk=pk)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'
    writer = csv.writer(response)
    columns =['Stock','Date']
    column_names = table.infos.all()

    columns=['Stock','Date']
    for header in column_names:
        columns.append(header.name)

    writer.writerow(columns)

    for row in table.row.all():
        row_data =[row.stock.symbol,row.date.date]
        for header in column_names:
            fd=row.stock.field_datas.get(info=header,table=table,date=row.date)
            row_data.append(fd.amount)
   
        writer.writerow(row_data)

    return response   