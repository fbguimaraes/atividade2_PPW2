from django.shortcuts import render
from django.http import HttpResponse
def email(request, email):
    return HttpResponse(f"O e-mail informado foi: {email}")
