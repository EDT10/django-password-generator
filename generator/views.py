from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # renders html file in the template folder and passes the dictionary (key value) to the html page
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*+)('))

    length = int(request.GET.get('length'))
    generate_password = ''

    for i in range(length):
        generate_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generate_password})

def about(request):
    return render(request, 'generator/about.html')