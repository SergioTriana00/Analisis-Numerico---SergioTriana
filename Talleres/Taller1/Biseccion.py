"""
Agosto 08 de 2021
@author: Diana Sofía Carrillo, Nelson Alejandro Mosquera y Sergio Esteban Triana
Método de Bisección
Análisis Numérico

"""

#LIBRERIAS
import numpy as np
import math


#FUNCIONES
def funcionA(x):
    return (np.cos(x)*np.cos(x)) - x**2 #cos^2(x) - x^2

def funcionB(x): 
    return (x*np.sin(x))-1 # xsen(x)-1, evaluar en [-1,2]

def funcionC(x):
    return (x**3)-(2*x**2)+((4/3)*x)-(8/27) #x^3-2x^2+4/3x-8/27

def funcionD(x): 
    return ((68.1*9.81)/x)*(1-(math.e)**(-(10/68.1)*x))-40 # 0 = (mg/x)*(1-e^-((t/m) * x))-v(t)

def funcionE(x): 
    return (x**3)-(2*x)-5 #x^3-2x-5=0

#METODO
def biseccion(funcion, a, b, eps):
    maxIteraciones = 5000 #Número máximo de iteraciones
    
    if funcion(a)*funcion(b) > 0 : #Se verifica que cumpla con el teorema del valor intermedio
        print('\t\tEl intervalo dado no contiene una raíz (cero) de la función')
        rta = [0]
        return rta
    
    for i in range (maxIteraciones):
        c = (a+b)/2
        
        if np.abs(funcion(c)) < eps:
            rta = [1, i+1, c]
            return rta
        
        if funcion(a)*funcion(c) < 0:
            b = c
        else:
            a = c

    if i == maxIteraciones - 1:
        rta = [2, i, c]
        return rta

#INVOCACIONES
print('\n----------------------------------------------------------------------------')
print('Funcion A:')
print('\tTorelancia 10E-8')
rta = biseccion(funcionA, 0, 1, 10E-8)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.8f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.8f}".format(rta[2]))

print('\tTorelancia 10E-16')
rta = biseccion(funcionA, 0, 1, 10E-16)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.16f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.16f}".format(rta[2]))

print('\tTorelancia 10E-32')
rta = biseccion(funcionA, 0, 1, 10E-32)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.32f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.32f}".format(rta[2]))

print('\tTorelancia 10E-56')
rta = biseccion(funcionA, 0, 1, 10E-56)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.56f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.56f}".format(rta[2]))


print('\n----------------------------------------------------------------------------')
print('Funcion B:')
print('\tTorelancia 10E-8')
rta = biseccion(funcionB, -1, 2, 10E-8)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.8f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.8f}".format(rta[2]))

print('\tTorelancia 10E-16')
rta = biseccion(funcionB, -1, 2, 10E-16)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.16f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.16f}".format(rta[2]))

print('\tTorelancia 10E-32')
rta = biseccion(funcionB, -1, 2, 10E-32)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.32f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.32f}".format(rta[2]))

print('\tTorelancia 10E-56')
rta = biseccion(funcionB, -1, 2, 10E-56)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.56f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.56f}".format(rta[2]))


print('\n----------------------------------------------------------------------------')
print('Funcion C:')
print('\tTorelancia 10E-8')
rta = biseccion(funcionC, 0, 1, 10E-8)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.8f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.8f}".format(rta[2]))

print('\tTorelancia 10E-16')
rta = biseccion(funcionC, -1, 0.7, 10E-16)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.16f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.16f}".format(rta[2]))

print('\tTorelancia 10E-32')
rta = biseccion(funcionC, -1, 0.7, 10E-32)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.32f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.32f}".format(rta[2]))

print('\tTorelancia 10E-56')
rta = biseccion(funcionC, -1, 0.7, 10E-56)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.56f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.56f}".format(rta[2]))


print('\n----------------------------------------------------------------------------')
print('Funcion D:')
print('\tTorelancia 10E-8')
rta = biseccion(funcionD, 14, 15, 10E-8)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.8f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.8f}".format(rta[2]))

print('\tTorelancia 10E-16')
rta = biseccion(funcionD, 14, 15, 10E-16)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.16f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.16f}".format(rta[2]))

print('\tTorelancia 10E-32')
rta = biseccion(funcionD, 14, 15, 10E-32)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.32f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.32f}".format(rta[2]))

print('\tTorelancia 10E-56')
rta = biseccion(funcionD, 14, 15, 10E-56)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.56f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.56f}".format(rta[2]))


print('\n----------------------------------------------------------------------------')
print('Funcion E:')
print('\tTorelancia 10E-8')
rta = biseccion(funcionE, 2, 3, 10E-8)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.8f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.8f}".format(rta[2]))

print('\tTorelancia 10E-16')
rta = biseccion(funcionE, 2, 3, 10E-16)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.16f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.16f}".format(rta[2]))

print('\tTorelancia 10E-32')
rta = biseccion(funcionE, 2, 3, 10E-32)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.32f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.32f}".format(rta[2]))

print('\tTorelancia 10E-56')
rta = biseccion(funcionE, 2, 3, 10E-56)
if rta[0] == 1:
    print('\t\tSe encontraron las raices en ' + str(rta[1]) + ' iteraciones. Su valor es: ' + "{:.56f}".format(rta[2]))
elif rta[0] == 2:
    print('\t\tSe ha llegado al número máximo de iteraciones. La raíz aproximada luego del máximo número de iteraciones es: ' + "{:.56f}".format(rta[2]))


