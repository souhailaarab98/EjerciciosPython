#!/usr/bin/env python
# -*- coding: utf-8 -*-

def imprimirdos(cadena):
    return cadena[:2]

def imprimirtresUlt(cadena):
    return cadena[-2:]
def imprimircadados(cadena):
    return cadena[::2]
def imprimirInverso(cadena):
    return cadena[::-1]
def imprimirdosSentidos(cadena):
    return (cadena + cadena[::-1])

print imprimirdos('Palabra')
print imprimirtresUlt('Palabra')
print imprimircadados('Palabra')
print imprimirInverso('Palabra')
print imprimirdosSentidos('Palabra')
