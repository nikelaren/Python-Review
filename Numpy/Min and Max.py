import numpy as np
N, M  = [int(i) for i in input().split()]
A = np.array([input().split() for i in range(N)], int)
print(np.max(np.min(A, axis = 1)), sep = "\n")