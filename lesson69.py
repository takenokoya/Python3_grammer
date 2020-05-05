# scilit-learn を使ったサンプルコード

from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt


# digits とは手書き数字画像のサンプルデータセット
digits = datasets.load_digits()
print(digits.keys())
print(digits.target[10])
plt.imshow(digits.images[10], cmap=plt.cm.gray_r, interpolation='nearest')
plt.savefig('./output2.png')


# Support Vector Machine
digits = datasets.load_digits()
# SVMクラスを初期化
model = svm.SVC(gamma=0.001, C=100.)
# index 3 以降のデータを教師データとしてSVMに学習させる
model.fit(digits.data[3:], digits.target[3:])
# index 3 以前のデータをSVMに予測させたものを出力
print(model.predict(digits.data[:3]))
# index 3 以前の実際のデータも出力
print(digits.target[:3])
plt.imshow(digits.images[2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.savefig('./output3.png')
