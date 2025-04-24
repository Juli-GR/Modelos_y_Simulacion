import numpy as np

N = 10000000

U = np.random.uniform(size=N)

def expression(u):
    x = 6*u -3
    return 6*x/(x-np.e**x)

suma = 0

for i in range(N):
    suma += expression(U[i])

print(suma/N)