# 値渡しと参照渡し
# リストや辞書型は参照渡し
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('j=', i)
print(id(j))
print(id(i))

# リストで値渡ししたいときは、copyメソッドを使う
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y=', y)
print('x=', x)
print(id(y))
print(id(x))

# 数字は値渡し
x = 20
y = x
y = 5
print(y)
print(x)
print(id(y))
print(id(x))