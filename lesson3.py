# 文字のメソッド
s = 'My name is Mike. Hi Mike'
print(s)

# Myで始まるか
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print('##################')
# find
print(s.find("Mike"))
print(s.rfind("Mike"))
print(s.count("Mike"))
# 最初のみ大文字
print(s.capitalize())
# 単語の最初のみ大文字
print(s.title())
# 大文字
print(s.upper())
# 小文字
print(s.lower())
# 置換
print(s.replace('Mike', 'Nancy'))
