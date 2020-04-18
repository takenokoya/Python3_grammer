# 変数宣言
num = 1
name = 'mike'
is_ok = True
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# intの変数にstrを代入も問題ない
num = name
print(num, type(num))

# cast 型変換
name = '1'
new_num = int(name)
print(new_num, type(new_num))

# とりあえずprint
# separation引数
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='\n')
