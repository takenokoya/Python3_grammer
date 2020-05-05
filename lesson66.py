# Numpy を使ったサンプルコード

import numpy as np

# numpy.ndarray
# 行列計算
x = np.array([1, 2, 3])
print(x.shape)
print(x)
print(x[0], x[1], x[2])
x[1] = 0
print(x)
print('###############')

x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]
x_array = np.array(x)
y_array = np.array(y)
print(x_array)
print(y_array)
# 内積を計算
print(np.dot(x, y))
