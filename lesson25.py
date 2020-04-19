# キーワード引数とデフォルト引数
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


# キーワード引数を指定して関数実行
menu(entree='beef', drink='beer', dessert='ice')
print('###########')


# デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


# 関数を実装
menu()
print('###########')
menu(entree='chicken')
print('###########')
menu('chicken', drink='beer')
print('###########')


# デフォルト引数で気をつけること
def test_func(x, l=[]):
    l.append(x)
    return l


y = [1, 2, 3]
r = test_func(100, y)
print(r)
print('###########')

y = [1, 2, 3]
r = test_func(200, y)
print(r)
print('###########')

r = test_func(100)
print(r)
print('###########')

# 下を実行すると [100, 100]
# listは参照渡しのため
# bugにつながるのでpythonでは、listやdictをデフォルト引数で与えるべきでない
r = test_func(100)
print(r)
print('###########')


# 解決法
# Noneを用いて、自分で初期化処理をする
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func(100)
print(r)
r = test_func(100)
print(r)