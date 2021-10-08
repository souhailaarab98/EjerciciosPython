#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tiempoEnSeg (hs, mn, seg):
    cantidad = hs * 3600 + mn * 60 + seg
    return cantidad
def tiempoHsMnSeg (x):
    hs = x / 3600
    min = ( x % 3600 ) / 60
    seg = ( x % 3600 ) % 60
    return (hs, min, seg)

horas = input("Horas?")
minutos = input("minutos?")
segundos = input("Segundos?")

tiempo1 = tiempoEnSeg(horas, minutos, segundos)
print ("el tiempo N 1 ", tiempo1)

horas = input("Horas?")
minutos = input("minutos?")
segundos = input("Segundos?")

tiempo2 = tiempoEnSeg(horas, minutos, segundos)
tiempoTotal = tiempo1 + tiempo2

print tiempoHsMnSeg(tiempoTotal)