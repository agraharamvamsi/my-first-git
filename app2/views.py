from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vijay (request):
    return HttpResponse('<h2>Vamsi is very good boy</2> ')

def pooja (request):
    return HttpResponse('<h4>pooja is good girl</h4>')
