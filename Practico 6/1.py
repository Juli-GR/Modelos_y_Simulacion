from utils import *

def calcular_estimadores_normal(N, d):
    return calcular_estimadores(N, d, np.random.normal)

print_estimadores(*calcular_estimadores_normal(100, 0.1))