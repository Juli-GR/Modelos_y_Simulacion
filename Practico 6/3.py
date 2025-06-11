import numpy as np
from math import sqrt
from utils import *

"""
El semiancho es 1.96 * sqrt(Scuad/n)
Queremos que sea menor que 0.001
Es basicamente usar calcular_estimadores con d = 0.001/1.96
"""

def formula_i(y):
    x = (y+1) * np.pi
    return np.sin(x)*np.pi/x

def ejercicio_i():
    return calcular_estimadores(1, 0.001/1.96, lambda: formula_i(np.random.uniform()))

print("Ejercicio i")
print_estimadores(*ejercicio_i())