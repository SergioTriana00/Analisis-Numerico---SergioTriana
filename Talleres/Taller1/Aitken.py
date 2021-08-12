# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:35:51 2021

@author: sergi
"""

import numpy as np
from bokeh.plotting import figure, output_file, show
from decimal import Decimal, getcontext
import math 


limite = 5000
def funcionuno(x):p
    return np.cos(x)**2-(x**2)

def funciondos(x): 
    return x*math.sin(x)-(1)

def funciontres(x):
    return x**3 - 2*(x**2) + (4/3)*x - (8/27)

def funcioncuatro(x): 
    e = math.e
    return  ((68.1*9.81)/x)*(1-(e)*(-(10/68.1)*x))-40

def funcioncinco(x): 
    return (x**3) - (2*x) - 5

def aitken(tol,x0,f, grafica, num_eq): 
    errores = []
    y_vals = []
    y_vals.append(x0)
    x1 = f(x0)
    errores.append(abs(x1-x0))
    y_vals.append(x1)
    x2 = f(x1)
    errores.append(abs(x2-x1))
    y_vals.append(x2)
    x3 = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)
    errores.append(abs(x3-x2))
    y_vals.append(x3)
    iterador = 3
    if(x3 != 0):
        while abs((x3-x0)/x3) > tol: 
            x0 = x3
            x1 = f(x0)
            errores.append(abs(x1-x0))
            y_vals.append(x1)
            x2 = f(x1)
            errores.append(abs(x2-x1))
            y_vals.append(x2)
            if  ((x2 - 2*x1 + x0) != 0): 
                x3 = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0) 
                errores.append(abs(x3-x2))
                y_vals.append(x3)
            iterador += 3
            if x3 == 0: 
                break
    x_vals = list(range(len(y_vals)))
    output_file(grafica + f"-{tol}.html")
    fig = figure()
    fig.line(x_vals, y_vals, line_width=2)
    if  x3 < 14:
        show(fig)
        x_errores = list(range(len(errores)))
        output_file(f'erroresSteffensen{num_eq}-{tol}.html')
        fig2 = figure()
        fig2.line(x_errores, errores, line_width=2)
        show(fig2)

    resultado = []
    resultado.append(iterador)
    resultado.append(x3)
    return resultado
        
            
if __name__ == "__main__": 
    getcontext().prec = 56
    tols = [10**-8, 10**-16, 10**-32, 10**-56]
    x = 0.7
    
    for tol in tols:  
        retorno = aitken(tol, x, funcionuno, "steffensen1",1)
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)} y {-1*Decimal(raiz)}')
    for tol in tols:  
        retorno = aitken(tol, x, funciondos, "steffensen2",2)
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')
   # for tol in tols:  
     #   retorno = aitken(tol, x, funciontres, "steffensen3",3)
     #   iteraciones = retorno[0]
     #   raiz = retorno[1]
     #   print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')
    for tol in tols:  
        retorno = aitken(tol, x, funcioncuatro, "steffensen4",4)
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {raiz}')
    for tol in tols:  
        retorno = aitken(tol, x, funcioncinco, "steffensen5",5)
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')
