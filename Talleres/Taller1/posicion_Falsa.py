import matplotlib.pyplot as plt
import math


def falsa_posicion(funcion, x_i, x_f, iteraciones, error_r):
    #Inicializar las variables
    solucion = None
    contador = 0
    erro_calculado = 101
    x1 = []
    x2 = []
    #Evaluar si la raiz esta dentro del intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
        #Calcular la solucion
        while contador <= iteraciones and erro_calculado >= error_r:
            x1.append(x_i)
            x2.append(x_f)
            contador += 1
            solucion = x_f - ((funcion(x_f) * (x_f - x_i)) / (funcion(x_f) - funcion(x_i)))
            error_calculado = abs((solucion - x_i) / solucion) * 100
            # Redefinir nuevo intervalo
            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion
        # Imprimir resultados
        return solucion
    else:
        print("Error: No existe la solucion en ese intervalo.")

solucion1 = falsa_posicion(lambda x: math.cos(x)**2 - x**2, 0, 1, 1000, 10**-8)
solucion2 = falsa_posicion(lambda x: math.cos(x)**2 - x**2, 0, 1, 10000, 10**-16)
solucion3 = falsa_posicion(lambda x: math.cos(x)**2 - x**2, 0, 1, 100000, 10**-32)
solucion4 = falsa_posicion(lambda x: math.cos(x)**2 - x**2, 0, 1, 1000000, 10**-56)
print("Solucion f(x) = cos(x)^2 - x^2:")
print('La solucion aproximada es (10^-8) : {:.8f}'.format(solucion1))
print('La solucion aproximada es (10^-16): {:.16f}'.format(solucion2))
print('La solucion aproximada es (10^-32): {:.32f}'.format(solucion3))
print('La solucion aproximada es (10^-56): {:.56f}'.format(solucion4))



solucion1 = falsa_posicion(lambda x: x * math.sin(x) - 1, -1, 2, 1000, 10**-8)
solucion2 = falsa_posicion(lambda x: x * math.sin(x) - 1, -1, 2, 10000, 10**-16)
solucion3 = falsa_posicion(lambda x: x * math.sin(x) - 1, -1, 2, 100000, 10**-32)
solucion4 = falsa_posicion(lambda x: x * math.sin(x) - 1, -1, 2, 1000000, 10**-56)
print("Solucion f(x) = xsin(x)-1:")
print('La solucion aproximada es (10^-8) : {:.8f}'.format(solucion1))
print('La solucion aproximada es (10^-16): {:.16f}'.format(solucion2))
print('La solucion aproximada es (10^-32): {:.32f}'.format(solucion3))
print('La solucion aproximada es (10^-56): {:.56f}'.format(solucion4))



solucion1 = falsa_posicion(lambda x: x**3 - 2*x**2 + (4*x)/3 - 8/27, 0, 1, 1000, 10**-8)
solucion2 = falsa_posicion(lambda x: x**3 - 2*x**2 + (4*x)/3 - 8/27, 0, 1, 10000, 10**-16)
solucion3 = falsa_posicion(lambda x: x**3 - 2*x**2 + (4*x)/3 - 8/27, 0, 1, 100000, 10**-32)
solucion4 = falsa_posicion(lambda x: x**3 - 2*x**2 + (4*x)/3 - 8/27, 0, 1, 1000000, 10**-56)
print("Solucion f(x) = x^3 - 2x^2 + 4x/3 - 8/27:")
print('La solucion aproximada es (10^-8) : {:.8f}'.format(solucion1))
print('La solucion aproximada es (10^-16): {:.16f}'.format(solucion2))
print('La solucion aproximada es (10^-32): {:.32f}'.format(solucion3))
print('La solucion aproximada es (10^-56): {:.56f}'.format(solucion4))


solucion1 = falsa_posicion(lambda x: x**3 - 2 * x - 5, 2, 3, 1000, 10**-8)
solucion2 = falsa_posicion(lambda x: x**3 - 2 * x - 5, 2, 3, 10000, 10**-16)
solucion3 = falsa_posicion(lambda x: x**3 - 2 * x - 5, 2, 3, 100000, 10**-32)
solucion4 = falsa_posicion(lambda x: x**3 - 2 * x - 5, 2, 3, 1000000, 10**-56)
print("Solucion f(x) = x^3 - 2x - 5:")
print('La solucion aproximada es (10^-8) : {:.8f}'.format(solucion1))
print('La solucion aproximada es (10^-16): {:.16f}'.format(solucion2))
print('La solucion aproximada es (10^-32): {:.32f}'.format(solucion3))
print('La solucion aproximada es (10^-56): {:.56f}'.format(solucion4))



