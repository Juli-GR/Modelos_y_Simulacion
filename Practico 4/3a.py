import numpy as np
from math import sqrt

N = [100, 1000, 10000, 100000]

def game():
    count = 11
    check = [0]*13
    check[0], check[1] = None, None
    iteraciones = 0
    while count > 0:
        u = sum(np.random.randint(1,7,2))
        if check[u] == 0:
            check[u] = 1
            count -= 1
        iteraciones += 1
    return iteraciones

esperanza = [0]*len(N)
esperanza2 = [0]*len(N)
idx = 0

for i in range(N[-1]):
    g = game()
    esperanza[idx] += g
    esperanza2[idx] += g**2
    if i in N:
        esperanza[idx+1] = esperanza[idx]
        esperanza2[idx+1] = esperanza2[idx]
        idx += 1

for i in range(len(N)):
    esperanza[i] /= N[i]
    esperanza2[i] /= N[i]
    print(f"N: {N[i]}")
    print(f"Esperanza: {esperanza[i]}\t\
            Desviación: {sqrt(esperanza2[i]-esperanza[i]**2)}\n"
         )

"""
Resultados:

N: 100
Esperanza: 58.92                    Desviación: 35.43576724158798

N: 1000
Esperanza: 61.845                   Desviación: 38.01974454148792

N: 10000
Esperanza: 61.1883                  Desviación: 35.93100114260665

N: 100000
Esperanza: 61.16607                 Desviación: 36.061649861800554
"""