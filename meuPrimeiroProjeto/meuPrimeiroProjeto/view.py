from django.http import HttpResponse
from django.shortcuts import render

#Ola Mundo com HttpResponse
def hello(request):
    return HttpResponse('Hello word!!!')

#Ola Mundo com render(pega um html)
def ola(request):
    return render(request,'index.html')


def article(request, year):
    return HttpResponse('O ano digitado foi: ' + str(year))

def lerDoBanco(nome):
    banco = [
        {'nome':'Higor','idade':24},
        {'nome':'Zulaianny','idade':22},
        {'nome':'Paulo','idade':20}
    ]
    for pessoa in banco:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome':'Pessoa não encontrada','idade': 0}

def buscar(request, nome):
    
    result = lerDoBanco(nome)
    
    if result['idade'] > 0:
        return HttpResponse('A idade dessa pessoa é ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse("Pessoa não encontrada")

def name(request, name):
    result = lerDoBanco(name)['idade']
    return render(request, 'name.html',{'v_idade':result})