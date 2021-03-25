from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


def test(request):
    return render(request,'test.html')


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserSignupForm(request.POST)
        print('xxxxxxxxxxxx')

        if sign_up_form.is_valid():
            print('a')
            sign_up_form.save()
            print('b')
            user = authenticate(username=sign_up_form.cleaned_data['username'], password=sign_up_form.cleaned_data['password1'])
            print('c')
            login(request, user)
            return render(request,'user_tables.html')
        else:
            return redirect('sign-up')

    else:
        sign_up_form = UserSignupForm()       
        context = {
            'sign_up_form': sign_up_form,
        }
        return render(request, 'sign_up.html', context)


def view_all_tables(request):
    return render(request,'user_tables.html')
 