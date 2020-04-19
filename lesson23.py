# 関数定義
def say_something():
    print('Hi')

# 関数の実行
# ()が必要
say_something()

# typeはNone
print(type(say_something()))

def say_something():
    s = 'hi'
    return s
# 返り値を代入して出力
result = say_something()
print(result)

# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

