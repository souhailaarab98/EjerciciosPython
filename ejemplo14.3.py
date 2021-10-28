#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Punto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Punto(5,7)
print p
print p.x
print p.y