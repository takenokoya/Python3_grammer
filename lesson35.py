# 辞書内for表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)
print('#########')

# 以下でも同様の結果を得られる
d = {x: y for x, y in zip(w, f)}
print(d)
print('#########')

