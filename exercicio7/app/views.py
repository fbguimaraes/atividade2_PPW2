from django.shortcuts import render
from django.http import HttpResponse
# Create y

def artigo(request, slug):
    return HttpResponse(f"Artigo: {slug.replace("-", " ").title()}")