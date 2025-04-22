

#np.array - Creating NumPy Array

import numpy as np

a = np.array([1, 2, 3])
print(a)

#2D and 3D
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

#dtype
d = np.array([1, 2, 3], dtype = float)
print(d)

#np.arange
arg = np.arange(1, 34, 4)
print(arg)

#With reshape
resp = np.arange(16).reshape(2, 2, 2, 2)
print(resp)

#np.ones and np.zeros
out = np.ones((3, 4))
print(out)

out2 = np.zeros((3, 4))
print(out2)

#np.linspace
out3 = np.linspace(-10, 10, 10, dtype = int)
print(out3)