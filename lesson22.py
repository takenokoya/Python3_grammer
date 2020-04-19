# 辞書をfor文で処理
d = {'x': 100, 'y': 200}

# valueのみ
for v in d:
    print(v)

# tuple in list
print(d.items())

# key, value
for k, v in d.items():
    print(k, ':', v)

