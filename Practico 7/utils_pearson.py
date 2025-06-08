import numpy as np
from math import *
from scipy.stats import chi2

def pearson_estimator(N: list[int], p: list[float]) -> float:
    """
    Calculates the Pearson estimator of a list of numbers.

    Parameters:
    N: list[int]
        The list of frequencies.
    p: list[float]
        The list of probabilities.

    Returns:
    float
        The Pearson estimator of the list of numbers.
    """
    assert len(N) == len(p)

    n = sum(N)
    return sum((N[i] - n * p[i]) ** 2 / (n * p[i]) for i in range(len(N)))


def pearson_p_value(t: float, df: int) -> float:
    """
    Calculates the p-value of the Pearson estimator.

    Parameters:
    t: float
        The value of the Pearson estimator.
    df: int
        The degrees of freedom.

    Returns:
    float
        The p-value of the Pearson estimator.
    """
    return 1.0 - chi2.cdf(t, df)


def pearson_p_value_sim(t: float, n_sim: int, p: list[float], n: int):
    """
    Calculates the p-value of the Pearson estimator using simulation.

    Parameters:
    t: float
        The value of the Pearson estimator.
    n_sim: int
        The number of simulations to run.
    p: list[float]
        The list of probabilities.
    n: int
        The size of the original sample.

    Returns:
    float
        The p-value of the Pearson estimator.
    """
    def create_observation_freq(n: int, p: list[float]):
        N = np.zeros(len(p))
        N[0] = np.random.binomial(n, p[0])
        for i in range(1, len(p) - 1):
            N[i] = np.random.binomial(
                n - sum(N[:i]), p[i]/(1 - sum(p[:i]))
            )
        N[-1] = n - sum(N[:-1])
        return np.array(N, dtype=int)

    p_value = 0
    for _ in range(n_sim):
        N = create_observation_freq(n, p)
        t_sim = pearson_estimator(N, p)
        if t_sim >= t:
            p_value += 1
    return p_value / n_sim