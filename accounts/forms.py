from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username=forms.CharField(help_text='')            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None

                