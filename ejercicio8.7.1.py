#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cantidadCoincidencias(lista, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador

def posicionDePrimera(lista, elemento):
    posicion = 0
    encontrado = False
    for i in lista:
        if i == elemento and encontrado == False:
            return posicion
            encontrado = True
        posicion += 1

def listaPosiciones(lista, elemento):
    lista2 = []
    posicion = 0
    for i in lista:
        if i == elemento:
            lista2.append(posicion)
        posicion += 1
    return lista2

listaDeso = [7, 8, 9, 4, 15, 14, 2, 0, 4, 4, 3]
elemento = 4

print cantidadCoincidencias(listaDeso, elemento)
print posicionDePrimera(listaDeso, elemento)
print listaPosiciones(listaDeso, elemento)