# タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

# 通常の変数の値入れ替え
i = 10
j = 20
print(i, j)
tmp = i
i = j
j = tmp
print(i, j)

# タプルのアンパッキングを利用した変数の値入れ替え
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
