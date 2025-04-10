import numpy as np
N = [1000, 5000, 10000]

def expression(x, y):
    return np.e ** (x+y) ** 2

expected = 4.89916

suma = [0]*len(N)
i_suma = 0
u1 = np.random.uniform(size=N[-1])
u2 = np.random.uniform(size=N[-1])

for i in range(N[-1]):
    suma[i_suma] += expression(u1[i], u2[i])
    if i in N:
        suma[i_suma+1] = suma[i_suma]
        i_suma += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {suma[i]/n}")