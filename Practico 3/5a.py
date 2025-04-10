import numpy as np
N = [1000, 5000, 10000]

def expression(x):
    return (1-x**2)**(3/2)

expected = 3*np.pi/16

suma = [0]*len(N)
i_suma = 0
u = np.random.uniform(size=N[-1])

for i, k in enumerate(u):
    suma[i_suma] += expression(k)
    if i in N:
        suma[i_suma+1] = suma[i_suma]
        i_suma += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {suma[i]/n}")