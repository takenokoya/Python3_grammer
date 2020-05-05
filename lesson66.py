# Numpy を使ったサンプルコード

import numpy as np

# numpy.ndarray
x = np.array([1, 2, 3])
print(x.shape)
print(x)
print(x[0], x[1], x[2])
x[1] = 0
print(x)