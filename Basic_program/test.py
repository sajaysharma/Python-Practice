import numpy as np

arr = np.arange(27).reshape(3, 3, 3)

print(arr)

# print(arr[[0, 1], [2, 0], 1:3])

print(arr[[2, 2], [1, 2], 1:])