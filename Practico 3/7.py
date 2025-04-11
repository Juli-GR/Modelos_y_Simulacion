import numpy as np

N = [100, 1000, 10000, 100000, 1000000]

def expression():
    suma_1 = 0
    count = 0
    while suma_1 <= 1:
        suma_1 += np.random.uniform()
        count += 1
    return count

expected = np.e

suma = [0]*len(N)
i_suma = 0

for i in range(N[-1]):
    suma[i_suma] += expression()
    if i in N:
        suma[i_suma+1] = suma[i_suma]
        i_suma += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {suma[i]/n}")