from .models import *
from django import forms
from django.utils.timezone import now


class DateInput(forms.DateInput):
    input_type='date'


class TableCreationForm(forms.Form):
   table_name = forms.CharField(max_length=100)
   low_of_day = forms.BooleanField(initial=True,required=False)
   high_of_day = forms.BooleanField(initial=True,required=False)
   volume = forms.BooleanField(initial=True,required=False)
   open_price = forms.BooleanField(initial=True,required=False)
   closing_price = forms.BooleanField(initial=True,required=False)
   exchange =forms.BooleanField(initial=True,required=False)
   daily_range = forms.BooleanField(initial=True,required=False)
   daily_range_percent = forms.BooleanField(initial=True,required=False)
   open_pre_market = forms.BooleanField(initial=True,required=False)
   close_after_hours = forms.BooleanField(initial=True,required=False)
   industry = forms.BooleanField(initial=True,required=False)
   sector = forms.BooleanField(initial=True,required=False)
   market_cap = forms.BooleanField(initial=True,required=False)
   open_close_dif = forms.BooleanField(initial=True,required=False)
   open_close_perc = forms.BooleanField(initial=True,required=False)
   

class RowAdditionForm(forms.Form):
   ticker=forms.CharField(max_length=5,widget=forms.TextInput(attrs={'placeholder':'Ticker'}))
   date=forms.DateField(initial=now,widget=DateInput)    


