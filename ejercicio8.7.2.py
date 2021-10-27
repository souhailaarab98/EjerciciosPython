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


lista = [5, 8, 9, 16, 5, 45, 0, 3]
print valorMax(lista)
print maxPos(lista)