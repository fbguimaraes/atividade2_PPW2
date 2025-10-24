from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def arquivo(request, nome, ext):

    return HttpResponse(f"Arquivo recebido: {nome}.{ext}")

