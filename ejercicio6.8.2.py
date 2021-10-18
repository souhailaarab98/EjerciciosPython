#!/usr/bin/env python
# -*- coding: utf-8 -*-

def separar(palabra):
    palabra2 = ""
    for i in range(len(palabra)):
        palabra2 = palabra2 + palabra[i] + ','
    return palabra2

def reemplacarEspacio(frase):
    return frase.replace(" ", "\_")

def reemplacarDigitos(frase):
    frase2 = ""
    for i in range(len(frase)):
        if frase[i].isdigit():
            frase2 = frase2 + 'X'
        else:
            frase2 = frase2 + frase[i]
    return frase2
def insertar(number):
    number2 = ""
    for i in range(len(number)):
        if i % 3 ==0 and i != 0:
            number2 = number2 + '.' + number[i]
        else:
            number2 = number2 + number[i]
    return number2

print separar('Hola')
print reemplacarEspacio('Hola  A Todo El Mundo')
print reemplacarDigitos('Hola a los 155 alumnos')
print insertar('255255255')
