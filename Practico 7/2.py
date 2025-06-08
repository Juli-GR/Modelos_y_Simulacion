from utils_pearson import *

# DATA
p = [1/6]*6
N = [158, 172, 164, 181, 160, 165]

# Item A
t = pearson_estimator(N, p)
p_value = pearson_p_value(t, len(p) - 1)
print(f'p-value: {p_value}')

# Item B
n_sim = 1000
p_value_sim = pearson_p_value_sim(t, n_sim, p, sum(N))
print(f'p-value (simulation): {p_value_sim}')