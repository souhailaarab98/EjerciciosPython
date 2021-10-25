#!/usr/bin/env python
# -*- coding: utf-8 -*-

def comprobarOrden(tupla):
    if  tuple(sorted(tupla, reverse=True)) == tupla:
        return "esta ordenada de menor a mayor"
    elif tuple(sorted(tupla)) == tupla1:
        return "esta ordenada de mayor a menor"
    else:
        return "no esta ordenada "

tupla1 = ('5', '8', '1', '15', '10')

print comprobarOrden(tupla1)