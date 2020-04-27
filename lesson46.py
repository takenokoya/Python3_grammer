# 標準ライブラリ
# collections
# dafultdict

s = 'fjkajsdfhjioasufdiouaijed;jaja;'

# 辞書型のキーがない場合はvalue = 0 で キーバリューを作成
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

# setdafaultメソッドで初期化しても同じ結果
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)


# 標準ライブラリのdefaultdictを利用するとこんな感じ
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1

print(d)
