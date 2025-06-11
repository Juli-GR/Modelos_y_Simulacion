import numpy as np

matrix = np.array([[0.25, 0.5, 0.25], [0.5, 0, 0.5], [0.5, 0, 0.5]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)

for eigv in eigenvalues:
    print(round(eigv, 8))