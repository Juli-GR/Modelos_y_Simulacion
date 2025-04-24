import numpy as np
N = [1000, 5000, 10000]

def expression(x, y):

    exp = 1/x + 1/y -2
    div = 1/(x**2 * y**2)
    return np.e ** (exp) / div

expected = "idk"

suma = [0]*len(N)
i_suma = 0
u1 = np.random.uniform(size=N[-1])

for i in range(N[-1]):
    suma[i_suma] += expression(u1[i], np.random.uniform(u1[i],1) )
    if i in N:
        suma[i_suma+1] = suma[i_suma]
        i_suma += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {suma[i]/n}")