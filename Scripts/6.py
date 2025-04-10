import numpy as np
N = [1000, 10000, 100000]

def insideCircle(x, y):
    return np.sqrt(x**2 + y**2) <= 1

expected = np.pi

count = [0]*len(N)
i_count = 0
u1 = np.random.uniform(low=-1.0, high=1.0, size=N[-1])
u2 = np.random.uniform(low=-1.0, high=1.0, size=N[-1])

for i in range(N[-1]):
    if insideCircle(u1[i], u2[i]): count[i_count] += 1
    if i in N:
        count[i_count+1] = count[i_count]
        i_count += 1

print(f"Expected value: {expected}")
for i, n in enumerate(N):
    print(f"N={n}: {count[i]/n*4}")