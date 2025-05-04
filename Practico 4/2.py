import numpy as np
import time

N = 10000

def expression(u):
    return np.e**(u/N)

def expectedValue():
    r = 0
    for i in range(1, N+1):
        r += expression(i)
    return r

def inciso_b(n):
    U = np.random.randint(1,N+1, n)
    suma = 0
    for i in U:
        suma += expression(i)
    return suma*N/n

def inciso_c(n):
    r = 0
    for i in range(1, n+1):
        r += expression(i)
    return r

start_time = time.time()
expected = expectedValue()
time_expected = time.time() - start_time

start_time = time.time()
res_b = inciso_b(100)
time_b = time.time() - start_time

start_time = time.time()
res_c = inciso_c(100)
time_c = time.time() - start_time

print(f"Valor esperado: {expected}, sec: {time_expected}")
print(f"Inciso b: {res_b}, sec: {time_b}")
print(f"Inciso c: {res_c}, sec: {time_c}")