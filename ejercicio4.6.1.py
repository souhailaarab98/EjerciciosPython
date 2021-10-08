#!/usr/bin/env python
# -*- coding: utf-8 -*-

def esPar(num):
    if num % 2 == 0:
        return "el numero es Par"
    else:
        return "el numero es impar"

def esPrimo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador = contador + 1
    if contador == 2:
        return "El numero es Primo"
    else:
        return "El numero no es Primo"
print esPar(4)
print esPrimo(7)