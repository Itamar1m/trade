from django import forms


choices =(('1','1'),('2','2'),('3','3'),('5','5'),('15','15'),('30','30'),('45','45'),('60','60'),('90','90'),)
class ChartTimeForm(forms.Form):
    chart_time_frame_in_minutes = forms.ChoiceField(choices=choices)

