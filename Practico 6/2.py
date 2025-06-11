import numpy as np
from math import sqrt
from utils import *

def formula_i(x):
    return (np.e**x) / sqrt(2*x)

def formula_ii(y):
    x = - np.log( 1/y - 1 )     # Convierte intervalo de (-inf,inf) a (0,1)
    return x**2 * np.e**(-x**2)

def ejercicio_i(N, d):
    return calcular_estimadores(N, d, lambda: formula_i(np.random.uniform()))

def ejercicio_ii(N, d):
    return calcular_estimadores(N, d, lambda: formula_ii(np.random.uniform()))


N = 100
d = 0.01

print("Ejercicio i")
print_estimadores(*ejercicio_i(N, d))

print()
print("Ejercicio ii")
print_estimadores(*ejercicio_ii(N, d))
