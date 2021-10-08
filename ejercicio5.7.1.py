#!/usr/bin/env python
# -*- coding: utf-8 -*-

def promNotas():
    total = 0
    contador = 0
    while True:
        num = input("introduce una nota(* para salir)")
        if num == 100:
            break
        elif num < 0:
            print "el numero debe ser de 0 a 10"
        elif num > 0:
            total = total + num
            contador = contador + 1
            num = raw_input("introduce otra nota(* para salir)")
    return total / contador

print promNotas()