# こう書くこともできるが非推奨
import collections, sys, os
# 標準ライブラリは一番上に書く(一行ずつ書く)
import collections
import sys
import os

# サードパーティライブラリは2番めに書く(一行開ける)
import termcolor

# 最後はローカルパッケージ(一行開ける)
import lesson_package

# インストールされた先
print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)

print(sys.path)