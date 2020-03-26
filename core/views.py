from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade ):
    return HttpResponse('<h1> Hello {} de {} anos </h1>'.format(nome,idade))

def soma (request, valor1, valor2):
    a = valor1 + valor2
    return HttpResponse('O resultado da soma de {} e {} é igual a {}'.format(valor1, valor2, a))

def subtracao (request, valor1, valor2):
    a = valor1 - valor2
    return HttpResponse('O resultado da subtração de {} e {} é igual a {}'.format(valor1, valor2, a))

def multiplicacao(request, valor1, valor2):
    a = valor1 * valor2
    return HttpResponse('O resultado da multiplicação de {} e {} é igual a {}'.format(valor1, valor2, a))

def divisao (request, valor1, valor2):
    a = valor1 / valor2
    return HttpResponse('O resultado da divisão de {} e {} é igual a {}'.format(valor1, valor2, a))