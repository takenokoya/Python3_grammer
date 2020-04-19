# 値渡しと参照渡し
# リストのコピーは参照渡し
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('j=', i)
print(id(j))
print(id(i))

# リストで参照渡しを避けたいときは、copyメソッドを使う
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y=', y)
print('x=', x)
print(id(y))
print(id(x))

# 辞書型のコピーも参照渡し
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

# 参照渡しを避けるためにはcopyメソッド
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# 数字のコピーは値渡し
x = 20
y = x
y = 5
print(y)
print(x)
print(id(y))
print(id(x))