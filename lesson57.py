s = """\
AAA
BBB
CCC
DDD
"""
# w+ 書き込み+読み込み
with open('text.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# r+ 読み込み+書き込み
with open('text.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)


# with open('text.txt', 'r') as f:
#     # print(f.read())
#     # while True:
#     #     chunk = 2
#     #     line = f.read(chunk)
#     #     print(line)
#     #     if not line:
#     #         break
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(14)
#     print(f.read(1))
#     f.seek(15)
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))