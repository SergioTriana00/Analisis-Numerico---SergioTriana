# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 07:24:07 2021

@author: sergio
"""


# Método de Gauss-Seidel
# solución de sistemas de ecuaciones
# por métodos iterativos

import numpy as np

# INGRESO
A = np.array([[4 , 3, -2],
              [3,  4  , -1],
              [0, -1, 4  ]])

B = np.array([0.254,-1.425,2.978])

diagonal = np.array([[ 4, 0., 0.],
                     [ 0., 4, 0.],
                     [ 0., 0., 4]])

superior = np.array([[ 4., 3, 0.],
                     [ 0., 4, -1],
                     [ 0., 0., 4]])

inferior = np.array([[ 4, 0., 0.],
                     [ 3, 4, 0.],
                     [ 0., -1, 4]])

U = superior - diagonal

M = np.dot(np.linalg.inv(inferior),U);M

np.linalg.eigvals(M)
print("El resultado del radio espectral es: ",np.max(abs(np.linalg.eigvals(M))))


X0  = np.array([0.,0.,0.])

tolera = 0.0000000000000001
iteramax = 100

# PROCEDIMIENTO

# Gauss-Seidel
tamano = np.shape(A)
n = tamano[0]
m = tamano[1]
#  valores iniciales
X = np.copy(X0)
diferencia = np.ones(n, dtype=float)
errado = 2*tolera

itera = 0
while not(errado<=tolera or itera>iteramax):
    # por fila
    for i in range(0,n,1):
        # por columna
        suma = 0 
        for j in range(0,m,1):
            # excepto diagonal de A
            if (i!=j): 
                suma = suma-A[i,j]*X[j]
        
        nuevo = (B[i]+suma)/A[i,i]
        diferencia[i] = np.abs(nuevo-X[i])
        X[i] = nuevo
    errado = np.max(diferencia)
    itera = itera + 1

# Respuesta X en columna
X = np.transpose([X])

# revisa si NO converge
if (itera>iteramax):
    X=0
# revisa respuesta
verifica = np.dot(A,X)

# SALIDA
print('respuesta X: ')
print(X)
print('verificar A.X=B: ')
print(verifica)