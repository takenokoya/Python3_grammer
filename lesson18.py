# while文とfor文
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

print('##########')

# for
# イテレータを読み込み、次々に処理
for i in some_list:
    print(i)

print('##########')

for s in 'abcde':
    print(s)

print('##########')
# for文でもbreak, continue可能
split = 'My name is Mike'.split(' ')
print(split)
for word in split:
    if word == 'name':
        continue
    if word == 'Mike':
        break
    print(word)
