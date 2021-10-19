# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:06:45 2021

@author: Diana Sofía Carrillo
"""
from sympy import*
from pylab import*
import numpy as np

def lagrange(x, t, u = None):
    n = len(x)
    t = Symbol('t')
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L*(t - x[j])/(x[i]-x[j])
        p = p + y[i]*L
        p = expand(p)
    if u == None:
        return p
    else:
        return p.subs(t, u)

x = [40, 50, 60, 70, 80]
y = [35, 83, 153, 193, 215]
p = lagrange(x, y)
print("Polinomio de interpolación: ",p)
valor = 55
r = lagrange(x, y, valor)
print("Polinomio evaluado en", valor, ":",r)

def f(t): return t**4/3750 - 101*t**3/1500 + 371*t**2/60 - 7181*t/30 + 3343
t = arange(30, 80)
plot(t, f(t))
plot(x, y, 'o')
grid(true)
show()


