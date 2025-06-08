from utils_kolmogorov import *
from utils_F import *

numbers = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]

# Ej 1
D = kolmogorov_estimator(numbers, uniform_F)
print(f'Kolmogorov estimator: {D}')

# Ej 2
n_sim = 1000
n = len(numbers)
p_value_sim = kolmogorov_p_value_sim(D, n_sim, n)
print(f'p-value (simulation): {p_value_sim}')