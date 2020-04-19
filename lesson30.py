# クロージャー
def outer(a, b):

    def inner():
        return a + b

    return inner


# 足し算はされない
# function outer.<locals>.inner at 0x10e1ee950
print(outer(1, 2))

# 関数を実行した返り値(足し算の結果)をresultに代入して、resultを出力
# 関数を宣言した時点ではまだinner関数は実行されない
f = outer(1, 2)
# ここで初めてinner関数実行
r = f()
print(r)


# もうひとつ例
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


# outer関数の実行
# inner関数のobjを返す、関数のobjを代入
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

# inner関数に引数を渡して実行
print(cal1(10))
print(cal2(10))
