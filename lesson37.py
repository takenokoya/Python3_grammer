# generator内for表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print('###########')

# tupleではないかと思うかもしれないが、typeを確認してみるとちゃんとgeneratorであることがわかる
# tuple にしたい場合
# g = tuple(i for i in range(10))
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print('###########')

