from utils_pearson import *
import numpy as np
from scipy.stats import binom

muestra = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
param_n = 8
param_p = sum(muestra)/(len(muestra)*param_n)

k = 9

N_i = [0]*k
p_i = [0]*k
for i in range(k):
    N_i[i] = muestra.count(i)
    p_i[i] = binom.pmf(i, param_n, param_p)

T = pearson_estimator(N_i, p_i)
m = 1 # parametros estimados
df = k - 1 - m
p_value = pearson_p_value(T, df)
print(f"p-valor pearson: {p_value}")


N_sim = 1000
p_value_sim = 0
for i in range(N_sim):
    datos = list(np.random.binomial(param_n, param_p, size=len(muestra)))
    param_p_sim = sum(datos)/(len(datos)*param_n)

    N_i = [0]*k
    p_i = [0]*k
    for i in range(k):
        N_i[i] = datos.count(i)
        p_i[i] = binom.pmf(i, param_n, param_p_sim)

    T_sim = pearson_estimator(N_i, p_i)

    if T_sim >= T:
        p_value_sim += 1

print(f"p-valor simulacion: {p_value_sim/N_sim}")
