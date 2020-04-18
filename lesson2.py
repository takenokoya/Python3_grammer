# 文字列
s = 'test'
print(s)

# エスケープについて
print("I don't know")
print('I don\'t know')
print('say "I don\'t kow"')
print("say \"I don\'t kow\"")
print('Hello. \nHow are you?')
# raw
print('C:\name\name')
print(r'C:\name\name')

# 空白行が発生
print('###############')
print("""
line1
line2
line3
""")
print('###############')

# 空白行をなくす
print('###############')
print("""\
line1
line2
line3\
""")
print('###############')

# 文字連結
print('Hi.' * 3 + 'Mike')
print('Py' + 'thon')
print('Py''thon')
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

# 文字列とスライス
word = 'python'
print(word[0])
print(word[1])
print(word[2:5])
print(word[-1])
print('###############')
print(word[:5])
print(word[2:])
word = 'j' + word[1:]
print(word)
print(word[:])

# 文字列長
n = len(word)
print(n)