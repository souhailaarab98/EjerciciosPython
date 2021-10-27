#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sonPrimos(lista):
    listaNueva = []
    for i in len(lista):
        for j in range(1, lista[i]):
            contador = 0
            if lista[i] % j == 0:
                contador += 1
        if contador == 2:
            listaNueva.append(lista[i])
    return listaNueva

lista = ['5', '7', '12', '13', '15', '18', '21', '23']
print sonPrimos(lista)