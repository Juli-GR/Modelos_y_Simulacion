import numpy as np

def uniform_F(x: float) -> float:
    if 0 <= x <= 1:
        return x
    elif x < 0:
        return 0
    else:
        return 1

def exp_F(x: float, lam: float) -> float:
    return 1 - np.exp(- lam * x)