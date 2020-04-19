# 引数に*argsを指定すると、可変長引数に対応できる
def say_something(word, *args):
    # 位置引数は必ずある前提
    print(word)
    # argsはある場合は順番に取り出して処理
    for arg in args:
        print(arg)


# 位置引数 + 可変長引数(タプル)
say_something('Hi')
print('###########')
# argはタプルに入る
say_something('Hi', 'Mike', 'Nance')
print('###########')

t = ("Mike Bits", "Nance Edward")
say_something('Hi!', *t)
