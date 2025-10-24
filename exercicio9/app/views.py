from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def site(request, dominio):
    return  HttpResponseRedirect(f"https://{dominio}")
