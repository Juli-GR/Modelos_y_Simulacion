import numpy as np
import collections
from time import time
import bisect

import probability_func as pf


# Calculamos cada inciso y lo mostramos en pantalla

probabilities = [.11, .14, .09, .08, .12, .10, .09, .07, .11, .09]
N = 100

c = max(probabilities)*len(probabilities)
start_time = time()
inciso_a = pf.aceptacion_rechazo(probabilities, c, N)
time_a = time() - start_time
print(f"A   error: {pf.estimation_error(probabilities, inciso_a):.7f},\t\
        sec: {time_a:.7f}")

c = 3
start_time = time()
inciso_b = pf.aceptacion_rechazo(probabilities, c, N)
time_b = time() - start_time
print(f"B   error: {pf.estimation_error(probabilities, inciso_b):.7f},\t\
        sec: {time_b:.7f}")

start_time = time()
inciso_c = pf.transformada_inversa(probabilities, N)
time_c = time() - start_time
print(f"C   error: {pf.estimation_error(probabilities, inciso_c):.7f},\t\
        sec: {time_c:.7f}")

start_time = time()
inciso_d = pf.urna(probabilities, N)
time_d = time() - start_time
print(f"D   error: {pf.estimation_error(probabilities, inciso_d):.7f},\t\
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