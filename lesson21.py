# zip関数を使う
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# rangeの場合
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# zip関数の場合
# indexを指定せずに使える
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

