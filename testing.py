import numpy as np

x = [[2, 3, 6, 1, 2], [3, 3, 7, 5, 4], [9, 7, 6, 3, 1], [3, 9, 3, 0, 5]]
for i in range(4): x[i] = [sum(x[i])]
x = np.concatenate(x).tolist()
print(x)