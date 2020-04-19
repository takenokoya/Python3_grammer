# if
x = -10
# Pythonではintendはspace4つが暗黙のルール
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10
# pythonではintendでブロックを判別
if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')

