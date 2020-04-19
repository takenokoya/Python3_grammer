# input関数
while True:
    word = input("Enter1:")
    if word == 'ok':
        print('hit')
        break

# strでなくintで入力
while True:
    word = input("Enter2:")
    num = int(word)
    if num == 100:
        print('hit')
        break
