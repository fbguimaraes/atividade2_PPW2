from django.shortcuts import render
from django.http import HttpResponse

def produto(request, nome):
    return HttpResponse(f"Produto: {nome.replace('-', ' ').title()}.")