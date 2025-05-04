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


# Calculamos cada inciso y lo mostramos en pantalla

probabilities = [.11, .14, .09, .08, .12, .10, .09, .07, .11, .09]
N = 100

c = max(probabilities)*len(probabilities)
start_time = time.time()
inciso_a = aceptacion_rechazo(probabilities, c, N)
time_a = time.time() - start_time
print(f"A   error: {estimation_error(probabilities, inciso_a):.7f},\t\
        sec: {time_a:.7f}")

c = 3
start_time = time.time()
inciso_b = aceptacion_rechazo(probabilities, c, N)
time_b = time.time() - start_time
print(f"B   error: {estimation_error(probabilities, inciso_b):.7f},\t\
        sec: {time_b:.7f}")

start_time = time.time()
inciso_c = transformada_inversa(probabilities, N)
time_c = time.time() - start_time
print(f"C   error: {estimation_error(probabilities, inciso_c):.7f},\t\
        sec: {time_c:.7f}")

start_time = time.time()
inciso_d = urna(probabilities, N)
time_d = time.time() - start_time
print(f"D   error: {estimation_error(probabilities, inciso_d):.7f},\t\
        sec: {time_d:.7f}")

"""
Para N = 100000
A   error: 0.0075200,           sec: 0.3865244
B   error: 0.0070000,           sec: 0.8033888
C   error: 0.0082800,           sec: 0.0169916
D   error: 0.0070600,           sec: 0.0049965
Logicamente todos tienen errores parecidos´
y que tienden a 0 con N grande
pues las funciones son todas generadores validos
Hay algunas mas eficientes que otras

Para N = 100 hay mas error pero tarda menos
"""