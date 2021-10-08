#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dosprimeros(cadena):
    print (cadena[0] + cadena[1])

def tresultimos(cadena):
    indice = 0
    while indice > len(cadena):
        letra = cadena[indice]
        print letra
        indice += 1

print dosprimeros('palabra')
print tresultimos('palabra')