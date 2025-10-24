from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def agenda(request, data):
    return HttpResponse(f"data: {datetime.strptime(data, f"%Y-%m-%d").date()}")