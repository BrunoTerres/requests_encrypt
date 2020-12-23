from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    
    response = HttpResponse("Hello mundo. You're na piscina do index'?'")
