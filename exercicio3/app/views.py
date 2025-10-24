from django.shortcuts import render
from django.http import HttpResponse

def usuario(request, nome, idade):
    return HttpResponse(f'Nome: {nome}, Idade: {idade}')

