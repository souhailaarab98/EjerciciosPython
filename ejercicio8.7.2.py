#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valorMax(lista):
    maximo = 0
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

def maxPos(lista):
    maximo = 0
    posicion = 0
    posMax = 0
    for i in lista:
        if i > maximo:
            maximo = i
            posMax = posicion
        posicion += 1
    return maximo, posMax

def maxCadena(lista):
    maximo = ""
    posicion = 0
    posMax = 0
    for i in lista:
        if len(i) > len(maximo):
            maximo = i
            posMax = posicion
        posicion += 1
    return maximo, posMax

lista = [5, 8, 9, 16, 5, 45, 0, 3]
listaCadenas = ["hola", "Hola", "aaazedaajsnn", "ajsas", "haize", "ajzldd5"]
print valorMax(lista)
print maxPos(lista)
print maxCadena(listaCadenas)