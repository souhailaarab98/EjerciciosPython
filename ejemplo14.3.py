#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Punto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def es_numero(valor):
    return isinstance(valor, (int, float, long, complex) )

def __init__(self, x=0, y=0):
    """ Constructor de Punto, x e y deben ser numéricos,
        de no ser así, se levanta una excepción TypeError """
    if es_numero(x) and es_numero(y):
        self.x=x
        self.y=y
    else:
        raise TypeError("x e y deben ser valores numéricos")

def distancia(self, otro):
    """ Devuelve la distancia entre ambos puntos. """
    dx = self.x - otro.x
    dy = self.y - otro.y
    return (dx*dx + dy*dy)**0.5
def restar(self, otro):
    """ Devuelve un nuevo punto, con la resta entre dos puntos. """
    return Punto(self.x - otro.x, self.y - otro.y)
def norma(self):
    """ Devuelve la norma del vector que va desde el origen
        hasta el punto. """
    return (self.x*self.x + self.y*self.y)**0.5
    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """ Devuelve la resta de ambos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)
    print p + h
    print p - h
p = Punto(5,7)
a = Punto(8,9)
q = Punto(2,3)
t = Punto(1,4)
h = Punto(10, 11)
s = Punto(10, 10)
z = restar(p, h)



