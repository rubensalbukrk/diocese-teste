from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')