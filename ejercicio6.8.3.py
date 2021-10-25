#!/usr/bin/env python
# -*- coding: utf-8 -*-

def separar(palabra, maximo):
    palabra2 = ""
    contador = 0
    for i in range(len(palabra)):
        while  contador < maximo:
            palabra2 = palabra2 + palabra[i] + ','
            contador += 1
    return palabra2

def reemplacarEspacio(frase):
    return frase.replace(" ", "\_")

def reemplacerDigitos(frase, maximo):
    frase2 = ""
    contador = 0
    for i in range(len(frase)):
        while contador < maximo:
            if frase[i].isdigit():
                frase2 = frase2 + 'X'
            else:
                frase2 = frase2 + frase[i]
            contador += 1
    return frase2
def insertar(number, maximo):
    number2 = ""
    contador = 0
    for i in range(len(number)):
        while contador < maximo:
            if i % 3 ==0 and i != 0:
                number2 = number2 + '.' + number[i]
            else:
                number2 = number2 + number[i]
            contador += 1
    return number2

maximo = 1
print separar('Hola', maximo)
print reemplacarEspacio('Hola  A Todo El Mundo')
print reemplacerDigitos('Hola a los 155 alumnos', maximo)
print insertar('255255255', maximo)
