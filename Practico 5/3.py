import numpy as np

N = 100000

M = 3
exp_params = [3, 5, 7]
ps = [0.5, 0.3, 0.2]
assert(len(exp_params) == len(ps) and len(ps) == M)

expected_value = sum([b/a for a, b in zip(exp_params, ps)])

U = []
for param in exp_params:
    U.append(np.random.exponential(scale=1/param, size=N))

res = [0]*N
for i in range(N):
    for j in range(M):
        res[i] += ps[j] * U[j][i]

print(f"expected: {expected_value}")
print(f"estimation: {sum(res)/N}")