import matplotlib.pyplot as plt
import numpy as np

def plot_point_intervals(points, num_intervals):
    counts, bins = np.histogram(points, bins=num_intervals)
    plt.hist(points, bins=bins, edgecolor='black')
    plt.xlabel('Interval')
    plt.ylabel('Count')
    plt.title('Points per Interval')
    plt.show()

N = 1000000
I = 50

U = np.random.uniform(size=N)
points = []
max = -10

for i in range(N):
    u = U[i]
    if u < 1/16:
        value = np.log(16*u)/4
    else:
        value = 4*u - 0.25
        if max < value: max = value
    points.append(value)

plot_point_intervals(points, I)