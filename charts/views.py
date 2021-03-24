from django.shortcuts import render
from.models import *

def chart(request):
    
    return render(request,'chart.html')
