from django.shortcuts import render
from django.http import HttpResponse

def lista_posts(request):
    return HttpResponse(" Lista de posts do blog.")


def post(request, ano, mes, slug):

    ano = int(ano)
    mes = int(mes)

    if not (2000 <= ano <= 2030):
        return HttpResponse(" Ano inválido! O ano deve estar entre 2000 e 2030.")

  
    if not (1 <= mes <= 12):
        return HttpResponse(" Mês inválido! O mês deve estar entre 01 e 12.")

   
    return HttpResponse(f" Exibindo o post '{slug.replace("-", " ").title()}' publicado em {mes:02d}/{ano}.")
