# Matplotlibを使ったサンプルコード

import matplotlib.pyplot as plt
import numpy as np


# arrange は一定の間隔で数値を刻むndarrayを生成(0〜10まで0.1刻みのndarrayを生成)
x = np.arange(0, 10, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig('./output.jpg')