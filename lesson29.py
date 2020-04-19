# 関数内関数 # 関数の中でだけある関数を使いたい
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)

