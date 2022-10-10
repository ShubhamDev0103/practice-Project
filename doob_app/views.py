from calendar import c, month
from distutils.log import error
from email.errors import ObsoleteHeaderDefect
from fileinput import filename
from telnetlib import LOGOUT
from turtle import st, title
from webbrowser import get
from django.shortcuts import render,redirect
from requests import Response
from .forms import *
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import Group
from .models import *
import re
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework import status
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext, gettext_lazy as _


# Create your views here.


def index(request):
    pas = request.user.password
    print(pas)
    details = {
        'items' : [],
        'token' : []
    }
    try:
        token = Token.objects.filter(user = request.user)
        for tokens in token:
            fetch = Profile.objects.filter(user = request.user)
            date_joined = request.user.date_joined
            date_joined.strftime("%d:%m:%y %H:M:S")
            last_login = request.user.last_login

        for i in fetch:
            details['items'].append({'address': i.Address, 'zip_code': i.zip_code, 'City': i.City, 'County': i.County, 'State': i.State, 'photo': i.profile_img, 'title': i.title}) 

            return render(request, 'index-photographer.html', {'details': details['items'], 'date_joined' : date_joined, 'last_login': last_login, 'token': tokens})
    except:
        return render(request, 'index-photographer.html')

def login_(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

class Cus_Register(View):
    def get(self, request):
        form = Register()
        return render(request, 'Register.html', {'form': form})
    def post(self, request):
        form = Register(request.POST)
        if form.is_valid():   
            form.save()
            messages.success(request, 'Account Is Credited')
            return redirect('Login')
        return render(request, 'Register.html', {'form': form})

class Cus_Profile(View):
    def get(self, request):
        form = Profile_form()
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
            form = Profile_form(request.POST, request.FILES or None)
            if form.is_valid():
                user = request.user
                Address = form.cleaned_data['Address']
                county = form.cleaned_data['County']
                city = form.cleaned_data['City']
                state = form.cleaned_data['State']
                zip_code = form.cleaned_data['zip_code']
                title = form.cleaned_data['title']
                profile_img = form.cleaned_data['profile_img']
                fs = FileSystemStorage()
                filename = fs.save(profile_img.name, profile_img)
                url = fs.url(filename)
                reg = Profile(County = county, City = city, State = state, zip_code = zip_code, title = title,user = user, profile_img = url, Address = Address)
                reg.save()
                messages.success(request, 'Profile Create Successfully')
                return redirect('home_page')
            return render(request, 'profile.html', {'form': form, 'error': error})

def delete(request):
    request.user.auth_token.delete()
    return redirect('home_page')
