# 複数行コメント
"""
test
test
test
"""

# 途中改行
# 80文字で次の行にいくべき
s = 'aaaaaaaaaa' + 'bbbbbbbbbbbb'
print(s)
s = 'aaaaaaaaaa' \
    + 'bbbbbbbbbbbb'
print(s)
s = ('aaaaaaaaaa'
     + 'bbbbbbbbbbbb')
print(s)
