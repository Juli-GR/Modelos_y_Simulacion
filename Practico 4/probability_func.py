import numpy as np
import collections
import time
import bisect

"""
Estima el error entre la lista de probabilidades l1
y la generacion de N numeros aleatorios en l2
"""
def estimation_error(l1, l2):
    counter_l2 = collections.Counter(l2)
    error = 0
    for i in range(len(l1)):
        if(i in counter_l2):
            error += abs(l1[i] - counter_l2[i]/len(l2))
        else:
            error += l1[i]
    return error


# Funciones de probabilidad

def aceptacion_rechazo(l, c, size=1):
    res = []
    for i in range(size):
        while True:
            y = np.random.randint(0,len(l))
            u = np.random.uniform()
            condition = u < l[y]*len(l)/c
            if condition:
                res.append(y)
                break
    if size == 1:
        return res[0]
    else:
        return res

def transformada_inversa(l, size=1):
    acumulada = l.copy()
    for i in range(1,len(acumulada)):
        acumulada[i] += acumulada[i-1]
    res = []
    U = np.random.uniform(size=size)
    for i in range(size):
        res.append(bisect.bisect_left(acumulada, U[i]))
    if size == 1:
        return res[0]
    else:
        return res

def urna(l, size=1):
    urna = [i for i, k in enumerate(l) for _ in range(int(k*100))]
    assert(len(urna) == 100)

    res = []
    U = np.random.randint(0,100,size)
    for i in U:
        res.append(urna[i])
    if size == 1:
        return res[0]
    else:
        return res