from django.shortcuts import render, HttpResponse

def hello(request, nome, idade):
    return HttpResponse('<h1>Olá {} de {} anos</h1>'.format(nome, idade))

def soma (request, numero1, numero2):
    total = numero1 + numero2
    return HttpResponse('<h1>A soma de {} + {} = {} </h1>'.format(numero1, numero2, total))

def subtracao (request, numero1, numero2):
    total = numero1 - numero2
    return HttpResponse('<h1>A subtração de {} - {} = {} </h1>'.format(numero1, numero2, total))

def multiplicacao (request, numero1, numero2):
    total = numero1 * numero2
    return HttpResponse('<h1>A multiplicação de {} * {} = {} </h1>'.format(numero1, numero2, total))

def divisao (request, numero1, numero2):
    total = numero1 / numero2
    return HttpResponse('<h1>A divisao de {} / {} = {} </h1>'.format(numero1, numero2, total))

