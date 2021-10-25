#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fichasEncajan(tupla1, tupla2):
    if tupla1[0] == tupla2[0] or tupla1[0] == tupla2[1] or tupla1[1] == tupla2[1] or tupla1[1] == tupla2[0]:
        return "Las fichas se encajan"
    else:
        return "Las fichas no se encajan"

def fichasEncajan2(conjunto1, conjunto2):
    tupla1 = conjunto1.split("-")
    tupla2 = conjunto2.split("-")
    if tupla1[0] == tupla2[0] or tupla1[0] == tupla2[1] or tupla1[1] == tupla2[1] or tupla1[1] == tupla2[0]:
        return "Las fichas se encajan"
    else:
        return "Las fichas no se encajan"
tupla1 = ('4', '8')
tupla2 = ('9', '4')
print fichasEncajan(tupla1, tupla2)

conjunto = "4-5"
conjunto2 = "8-5"
print fichasEncajan2(conjunto, conjunto2)