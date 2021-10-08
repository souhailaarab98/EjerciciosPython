#!/usr/bin/env python
# -*- coding: utf-8 -*-

def canSeg (horas, min, seg):
    cantidad = horas * 3600 + min * 60 + seg
    return cantidad
def tiempoHsMnSeg (x):
    hs = x / 3600
    min = ( x % 3600 ) / 60
    seg = ( x % 3600 ) % 60
    return (hs, min, seg)
print canSeg(1, 1, 1)
print tiempoHsMnSeg(3661)