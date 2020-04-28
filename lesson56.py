# ファイルの作成や上書き
f = open('text.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
f.close()