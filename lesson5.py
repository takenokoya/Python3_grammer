# リストのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3]
# 3番めのindexからはじめて3番目のindex
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

if 100 in r:
    print('exist')

print(r)
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
# separatorがない
to_split = s.split('!!!')
print(to_split)
# separatorがある
to_split = s.split(' ')
print(to_split)

# separatorを使って結合する
x = ' '.join(to_split)
print(x)

# help関数
# print(help(list))
