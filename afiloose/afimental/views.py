from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def alagu(request):
    return HttpResponse('<h1> Alagu Vattu </h1>')