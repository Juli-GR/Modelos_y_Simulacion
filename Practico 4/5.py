from scipy.stats import binom
import numpy as np
from time import time

import probability_func as pf

# Funciones auxiliares

def estimation_error_bin(n, p, l):
    pmf = [binom.pmf(i, n, p) for i in range(n+1)]
    return pf.estimation_error(pmf, l)

def most_common_elem(l):
    return max(set(l), key=l.count)

def printAll(l):
    for e in l:
        print(e)
    print()

# Funciones de probabilidad adaptadas a la binomial

def transformada_inversa_bin(n, p, size=1):
    pmf = [binom.pmf(i, n, p) for i in range(n+1)]
    return pf.transformada_inversa(pmf, size=size)

def ensayos_bin(n, p, size=1):
    # Quizas pedian que lo hicieramos nosotros manualmente, ni idea
    return list(np.random.binomial(n, p, size))


n = 10
p = 0.3
N = 10000

start_time = time()
transformada_inversa = transformada_inversa_bin(n,p,N)
time_transformada_inversa = time() - start_time
printAll([
    f"transformada_inversa",
    f"error: {estimation_error_bin(n, p, transformada_inversa):.7f}",
    f"sec: {time_transformada_inversa:.7f}",
    f"most common element: {most_common_elem(transformada_inversa)}",
    f"porcentaje de:   0: {transformada_inversa.count(0)/N}   {n}: {transformada_inversa.count(n)/N}"
])

start_time = time()
ensayos = ensayos_bin(n,p,N)
time_ensayos = time() - start_time
printAll([
    f"ensayos",
    f"error: {estimation_error_bin(n, p, ensayos):.7f}",
    f"sec: {time_ensayos:.7f}",
    f"most common element: {most_common_elem(ensayos)}",
    f"porcentaje de:   0: {ensayos.count(0)/N}   {n}: {ensayos.count(n)/N}"
])

"""
Resultados

transformada_inversa
error: 0.0218331
sec: 0.0019996
most common element: 3
porcentaje de:   0: 0.0252   10: 0.0

ensayos
error: 0.0189493
sec: 0.0010018
most common element: 3
porcentaje de:   0: 0.0282   10: 0.0
"""