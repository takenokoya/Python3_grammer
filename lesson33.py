# generator
# 反復処理
l = ['Good morning', 'Good afternoon', 'Good night']

# forループの場合
for g in l:
    print(g)

print('#########')

# generatorを使う場合
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# numの数だけ yield 'run' するメソッド
def counter(num=10):
    for _ in range(num):
        yield 'run'

for g in greeting():
    print(g)

print('#########')

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))


