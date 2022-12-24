from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dinesh(request):
    return HttpResponse('<h1>Dinesh is placed in google</h1>')

def vignesh(request):
    return HttpResponse('<h2>Vamsi loves python</h2>')