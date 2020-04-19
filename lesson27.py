# キーワード引数の辞書化
def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='coffee')
# {'entree': 'beef', 'drink': 'coffee'}
print('#############')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
# 辞書を展開して引数に渡す
menu(**d)
