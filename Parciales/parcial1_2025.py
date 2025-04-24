import numpy as np
from math import sqrt

def monte_carlo_expression(u):
    x = 6*u +1
    return 6 * sqrt( x + sqrt(x) )

def monte_carlo(N):
    suma = 0
    u = np.random.uniform(size=N)
    for i in range(N):
        suma += monte_carlo_expression(u[i])
    print(f"N={N}: {suma/N}")

def juego():
    suma = 0
    count = 0
    while suma <= 1:
        suma += np.random.uniform()
        count += 1
    return count

def impares(N):
    count = 0
    for i in range(N):
        if juego() % 2 == 1: count += 1
    print(f"N={N}: {count/N}")


# Ejercicio 1
print("Ejercicio 1:")
N = [1000, 10000, 100000]
for n in N:
    monte_carlo(n)

# Ejercicio 2
print("")
print("Ejercicio 2:")
M = [100, 1000, 10000]
for m in M:
    impares(m)