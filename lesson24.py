

# 型指定する場合
# 引数の型、返り値の型の指定が可能。ただし、違う型でも例外とはならない
def add_num(a: int, b: int) -> int:
    return a + b


r = add_num(10, 20)
print(r)
# 30

r = add_num('a', 'b')
print(r)
# 'ab'
