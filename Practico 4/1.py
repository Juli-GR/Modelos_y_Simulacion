import numpy as np
import operator
from functools import reduce

N = [100, 1000, 10000, 100000]
r = 10
n = 100

def tirada_de_cartas():
    perm = np.random.permutation(range(1,n+1))
    coincidencias = sum(1 for i, num in enumerate(perm, start=1) if i == num)
    primeras_10 = (perm[:r] == range(1,r+1)).all()
    return coincidencias, primeras_10

expected = 1/reduce(operator.mul,range(n-r+1,n+1),1)    # 1/(100*99*...*91)

esperanza = [0]*len(N)
esperanza_2 = [0]*len(N)
inciso_a = [0]*len(N)
idx = 0

for i in range(N[-1]):
    coincidencias, primeras_10 = tirada_de_cartas()
    esperanza[idx] += coincidencias
    esperanza_2[idx] += coincidencias**2
    if primeras_10: inciso_a[idx] += 1
    if i in N:
        esperanza[idx+1] = esperanza[idx]
        esperanza_2[idx+1] = esperanza_2[idx]
        inciso_a[idx+1] = inciso_a[idx]
        idx += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print("")
    print(f"N={n}")
    print(f"esperanza: {esperanza[i]/n}")
    print(f"varianza: {(esperanza_2[i]/n)-(esperanza[i]/n)**2}")
    print(f"inciso_a: {inciso_a[i]/n}")