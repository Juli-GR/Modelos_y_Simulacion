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

masDe14 = [0]*len(N)    # debería ser muy alta
menosDe10 = [0]*len(N)  # deberia ser 0
idx = 0

for i in range(N[-1]):
    g = game()
    if g>14: masDe14[idx] += 1
    if g<9: menosDe10[idx] += 1
    if i in N:
        masDe14[idx+1] = masDe14[idx]
        menosDe10[idx+1] = menosDe10[idx]
        idx += 1

for i in range(len(N)):
    print(f"N: {N[i]}")
    print(f"Al menos 15: {masDe14[i]/N[i]}\t\
            A lo sumo 9: {menosDe10[i]/N[i]}\n"
         )

"""
Resultados:

N: 100
Al menos 15: 1.01                   A lo sumo 9: 0.0

N: 1000
Al menos 15: 1.0                    A lo sumo 9: 0.0

N: 10000
Al menos 15: 0.9983                 A lo sumo 9: 0.0

N: 100000
Al menos 15: 0.99865                A lo sumo 9: 0.0
"""