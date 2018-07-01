from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import calendar

def print_numbers():
    return str(calendar.February)

def index(request):
    return HttpResponse("Hello, world. You're at the games site." + print_numbers())