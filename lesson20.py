# range関数
for i in range(2, 10):
    print(i)

print('############')

# 2個飛ばしで出力したい
for i in range(2, 10, 2):
    print(i)

print('############')

# 3個飛ばしで出力したい
for i in range(2, 10, 3):
    print(i)

print('############')

# indexも出力
for i in range(10):
    print(i, 'hello')

print('############')

# indexがいらないことを明示的に表す_(アンダースコア)
for _ in range(10):
    print('hello')
