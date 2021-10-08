#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mayorProducto(n1, n2, n3, n4):
    p1 = n1 * n2
    p2 = n1 * n3
    p3 = n1 * n4
    p4 = n2 * n3
    p5 = n2 * n4
    p6 = n3 * n4

    if p1 > p2:
        if p1 > p3:
            if p1 > p4:
                if p1 > p5:
                    if p1 > p6:
                        return p1
    elif p2 > p1:
        if p2 > p3:
            if p2 > p4:
                if p2 > p5:
                    if p2 > p6:
                        return p2
    elif p3 > p1:
        if p3 > p2:
            if p3 > p4:
                if p3 > p5:
                    if p3 > p6:
                        return p3
    elif p4 > p1:
        if p4 > p2:
            if p4 > p3:
                if p4 > p5:
                    if p4 > p6:
                        return p4
    elif p5 > p1:
        if p5 > p2:
            if p5 > p3:
                if p5 > p4:
                    if p5 > p6:
                        return p5
    elif p6 > p1:
        if p6 > p2:
            if p6 > p3:
                if p6 > p5:
                    if p6 > p5:
                        return p6

num1 = input("Numero 1")
num2 = input("Numero 2")
num3 = input("Numero 3")
num4 = input("Numero 4")
y = mayorProducto(num1, num2, num3, num4)
print y