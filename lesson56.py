# ファイルの作成や上書き
with open('text.txt', 'w') as f:
    f.write('Test\n')
# withステートメントを使うことで、close()が不要となる
# f.close()