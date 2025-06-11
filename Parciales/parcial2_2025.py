import numpy as np

def funcion_1(x):
    return 30* (x**2 - 2*x**3 + x**4)

def ejercicio1():
    c = 1.875
    while True:
        Y = np.random.uniform()
        U = np.random.uniform()
        if U <= funcion_1(Y)/c:
            return Y

def codigoX(p):
    i = 10
    acumulada = p
    prob_i = p
    U = np.random.uniform()
    while True:
        if U <= acumulada:
            return i
        i += 1
        prob_i *= (1-p)
        acumulada+= prob_i

N = 10000

l1 = [0]*N
for i in range(N):
    l1[i] = ejercicio1()
print(f"ejercicio 1, valor esperado: {sum(l1)/N}")

p = 0.5
l2 = [0]*N
for i in range(N):
    l2[i] = codigoX(p)
print(f"ejercicio 2, valor esperado: {sum(l2)/N}")