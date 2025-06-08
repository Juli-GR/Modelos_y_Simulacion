from utils_kolmogorov import *
from utils_F import *
import scipy.stats as st

numbers = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]

scale = 50
lam = 1/50

# Ej 1
# D = kolmogorov_estimator(numbers, lambda x: exp_F(x, lam))    # Con F escrita por mi, pero mj usar scipy.stats
D = kolmogorov_estimator(numbers, lambda x: st.expon.cdf(x=x, scale=scale))
print(f'Kolmogorov estimator: {D}')

# Ej 2
n_sim = 1000
n = len(numbers)
p_value_sim = kolmogorov_p_value_sim(D, n_sim, n)
print(f'p-value (simulation): {p_value_sim}')