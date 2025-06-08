from utils_pearson import *
import numpy as np

# Hipótesis: La proporción del area de cada sector respecto a la rueda
# es la probabilidad de que dicho sector salga

p_i = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
N_i = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]

# Punto D: Pearson

T = pearson_estimator(N_i, p_i)
k = len(p_i)
df = k - 1
p_value = pearson_p_value(T, df)
print(f"p-valor pearson: {p_value}")

# Punto E: simulación

p_value_sim = pearson_p_value_sim(T, 1000, p_i, sum(N_i))
print(f"p-valor simulacion: {p_value_sim}")
