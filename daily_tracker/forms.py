from .models import *
from django import forms
from django.utils.timezone import now

class DateInput(forms.DateInput):
    input_type='date'


class TableCreationForm(forms.Form):
   table_name = forms.CharField(max_length=100,label=" ")
   low_of_day= forms.BooleanField(initial=True,required=False)
   high_of_day= forms.BooleanField(initial=True,required=False)
   volume=forms.BooleanField(initial=True,required=False)
   open_price=forms.BooleanField(initial=True,required=False)
   closing_price= forms.BooleanField(initial=True,required=False)

class RowAdditionForm(forms.Form):
   ticker=forms.CharField(max_length=5)
   date=forms.DateField(initial=now,widget=DateInput)    


#  table.infos.add(*form.cleaned_data['columns'])
     
#             return redirect('view-table',table.pk)


#    columns=forms.ModelMultipleChoiceField(queryset=InfoField.objects.all()) 