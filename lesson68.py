# Matplotlibを使ったサンプルコード

import matplotlib.pyplot as plt
import numpy as np


# arrange は一定の間隔で数値を刻むndarrayを生成(0〜10まで0.1刻みのndarrayを生成)
x = np.arange(0, 10, 0.1)
y = np.sin(x)
# subplot は画像を制御するクラスをグラフを制御するクラスを返す
fig, ax = plt.subplots()
# グラフaxに対して生成したndarrayをプロット
ax.plot(x, y)
# jpg画像として保存
plt.savefig('./output.jpg')