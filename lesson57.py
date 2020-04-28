s = """\
AAA
BBB
CCC
DDD
"""
with open('text.txt', 'w') as f:
    f.write(s)

with open('text.txt', 'r') as f:
    # print(f.read())
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break