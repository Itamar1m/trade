from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from daily_tracker.forms import *
from django.contrib.auth.decorators import login_required


def test(request):
    return render(request,'test.html')


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserSignupForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            user = authenticate(username=sign_up_form.cleaned_data['username'], password=sign_up_form.cleaned_data['password1'])
            login(request, user)
            return redirect('view-all-tables')
        else:
            return redirect('sign-up')

    else:
        sign_up_form = UserSignupForm()       
        context = {
            'sign_up_form': sign_up_form,
        }
        return render(request, 'sign_up.html', context)

@login_required(login_url='login' )
def view_all_tables(request):
    table_creation_form = TableCreationForm()

    return render(request,'user_tables.html',{'table_creation_form':table_creation_form})
 