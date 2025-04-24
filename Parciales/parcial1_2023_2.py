import numpy as np

N = 100000

A1 = np.random.uniform(size=N)
A2 = np.random.uniform(size=N)
B1 = np.random.uniform(size=N)
B2 = np.random.uniform(size=N)

def game(u):
    if (A1[i] > .5 and B1[i] < .5) or (not (B1[i] > .5 and A1[i] < .5) and (A2[i] > .5 and B2[i] < .5)):
        return True
    return False

count = 0

for i in range(N):
    if game(i): count += 1

print(count/N)