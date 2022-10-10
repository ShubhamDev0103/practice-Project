from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from tkinter.ttk import Style
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import TextInput, NumberInput, FileInput

from doob_app.models import Profile

class Register(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        labels = {'email': 'Email', 'first_name': 'First Name', 'last_name': 'Last Name'}
        widgets = {'username': TextInput(attrs={'class': 'form-control form-control-lg'})}  

class Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control form-control-lg'}))
    password = forms.CharField(label=_('Password'), strip=True, widget=forms.PasswordInput(attrs={'autocomplate': 'current-password', 'class': 'form-control form-control-lg'})) 

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['Address','County', 'State', 'City', 'zip_code', 'title', 'profile_img']
        widgets = {'City' : TextInput(attrs={'class': 'form-control form-control-lg'}),
        'Address' : TextInput(attrs={'class': 'form-control form-control-lg'}),
        'zip_code': TextInput(attrs= {'class': 'form-control form-control-lg'}), 
        'State' : TextInput(attrs={'class': 'form-control form-control-lg'}),
        'County' : TextInput(attrs={'class': 'form-control form-control-lg'}),
        'title' : TextInput(attrs={'class': 'form-control form-control-lg'}),
        'profile_img' : FileInput(attrs={'class': 'form-control form-control-lg', 'accept': '.jpg', 'style':'background-color: transparent; color: #acacac;'}),

        }

class Edit_Profile(ModelForm):
    class Meta:
        model = Profile
        fields = ['Address', 'County', 'State', 'zip_code']


class Admin_PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control form-control-lg'})),
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}), help_text=password_validation.password_validators_help_text_html()) 
    new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}),
    )


class Admin_PasswordReset(PasswordResetForm):
     email = forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control form-control-lg'}))


class Admin_New_Rest_Password(SetPasswordForm):
        new_password1 = forms.CharField(label=_("New password"),widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}),strip=False,help_text=password_validation.password_validators_help_text_html(),)
        new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg'}),
    )
