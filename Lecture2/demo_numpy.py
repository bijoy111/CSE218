import numpy as np

a = np.array([0,1,2])

# a = np.arange(9).reshape(2,3)

# np.zeros(), np.ones()

def func(x):
    x + 10

a = np.fromfunction(func, (3), dtype=int)

# np.sum(), np.max(), np.dot(), np.concat/concatenate()

print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.size)