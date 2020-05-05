# scilit-learn を使ったサンプルコード

from sklearn import datasets
import matplotlib.pyplot as plt


# digits とは手書き数字画像のサンプルデータセット
digits = datasets.load_digits()
print(digits.keys())
print(digits.target[10])
plt.imshow(digits.images[10], cmap=plt.cm.gray_r, interpolation='nearest')
plt.savefig('./output2.png')

