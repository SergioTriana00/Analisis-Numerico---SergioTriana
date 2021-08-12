# Aproximación Polinomio de Taylor
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO --------------------
x = sym.Symbol('x')
fx = (1/(1-x))

x0 = 0
n  = 1 # grado de polinomio

# Intervalo para Gráfica
a = -1
b = 1
muestras = 50

# PROCEDIMIENTO  -------------
# construye polinomio Taylor
k = 0 # contador de términos
polinomio = 0
while (k <= n):
    derivada   = fx.diff(x,k)
    derivadax0 = derivada.subs(x,x0)
    divisor   = np.math.factorial(k)
    terminok  = (derivadax0/divisor)*(x-x0)**k
    polinomio = polinomio + terminok
    k = k + 1

# forma lambda para evaluación numérica
fxn = sym.lambdify(x,fx,'numpy')
pxn = sym.lambdify(x,polinomio,'numpy')

# evaluar en intervalo para gráfica
xi = np.linspace(a,b,muestras)
fxi = fxn(xi)
pxi = pxn(xi)

# SALIDA  --------------------
print('polinomio p(x)= ')
print(1/polinomio)
print()

print(xi)

# Gráfica
plt.plot(xi,fxi,label='f(x)')
# franja de error


plt.axvline(x0,color='green', label='x0')
plt.axhline(0,color='grey')
plt.title('Polinomio Taylor: f(x) vs p(x)')
plt.legend()
plt.show()
