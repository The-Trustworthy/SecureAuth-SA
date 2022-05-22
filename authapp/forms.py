from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm
#########
from dataSecurity import *
from secureAuth import *


class UserRegistration(forms.ModelForm):
    thisSA = secureAuth()

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            else:
                dob = False
                fpPath = False
                cd['password2'] = thisSA.getEffectivePass(cd['password2'])
            return cd['password2']  # integrat pass #


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


