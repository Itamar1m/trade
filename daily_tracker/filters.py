from .models import *
import django_filters
from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class TableFilter(django_filters.FilterSet):
    stock__symbol = django_filters.CharFilter(lookup_expr='icontains',label='Ticker')
    date__date = django_filters.DateFilter(lookup_expr='exact',widget=DateInput(attrs={'class':'datepicker'}),label='Date')
   
    class Meta:
        model = UserCustomTableStocks
        fields =['stock__symbol','date__date']
     
    