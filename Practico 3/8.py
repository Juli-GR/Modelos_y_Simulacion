import numpy as np

N = [100, 1000, 10000, 100000, 1000000]

def expression():
    prod = 1
    count = 0
    while prod >= np.e ** (-3):
        prod *= np.random.uniform()
        count += 1
    return count

M = 7
j = range(M)
sum_j = [0]*M

def point_b(x):
    for i, k in enumerate(j):
        if x==k: sum_j[i] += 1

expected = 4

suma = [0]*len(N)
i_suma = 0

for i in range(N[-1]):
    res = expression()
    suma[i_suma] += res
    point_b(res)
    if i in N:
        suma[i_suma+1] = suma[i_suma]
        i_suma += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {suma[i]/n}")
for i, k in enumerate(sum_j):
    print(f"P(N={j[i]}): {k/N[-1]}")
