import numpy as np

N = 100000
U = np.random.uniform(low=0, high=1, size=N)

def expression(u):
    a3 = np.log(1/u +1)        # log es ln en numpy
    return 1/a3

suma = 0

for i in range(N):
    suma += expression(U[i])

print(suma/N)