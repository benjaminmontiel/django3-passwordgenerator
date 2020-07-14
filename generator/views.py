# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')



def password(request):


    characters= list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Mayuscula'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numeros'):
        characters.extend(list('0123456789'))
    if request.GET.get('Especiales'):
            characters.extend(list('|@#¢∞¬÷“”≠'))

    if request.GET.get('about'):
            return render(request,'generator/about.html')


    length= int(request.GET.get('length','14'))


    thepassword=''

    for x in range(length):
        thepassword+=random.choice(characters)



    return render(request,'generator/password.html',{'password':thepassword})
