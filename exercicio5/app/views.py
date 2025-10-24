from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def perfil(request, nome=None):
    if nome == None:
        return HttpResponse("Visitante!")
    else:
        return HttpResponse(f"Usuário: {nome}")
