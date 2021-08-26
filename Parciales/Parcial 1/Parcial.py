# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 07:24:07 2021

@author: sergio
"""


import numpy as np
import matplotlib.pyplot as plt


#Usa f(x) = x**3-2x-5
def f(x): 
    return (x**3-(3*x)-5)

def g(x): 
    return np.cbrt((3*x)+5)



def puntofijoParcial(Tol,a,b):
  if g(a)>a and g(b)<b: 
      xi = 0
      Error = np.abs(g(xi)-xi)
      i = 0 #Contador de iteraciones
            
      while (Error>Tol and i<=100):

        if i > 0:
          Error = np.abs(g(xi)-xi)

        xi=g(xi)
        i+=1
        
      print("La x, f(x)=0 es: {:.5f} ".format(xi))
      print("Iteraciones: ",i)      
  else:
    print("No se puedede realizar, funcion no converge")



x=np.linspace(start=-10, stop=10, num=100)
plt.ylim([-10,10])
plt.xlim([-2,4])
plt.grid()
plt.plot(x, f(x))
plt.axhline(y=0, linewidth=2, c='k')
plt.axvline(x=0, linewidth=2, c='k')
plt.show()
puntofijoParcial(1e-5,2,3)
