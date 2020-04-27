# Pythin3では以下の記述でもOK
# class Person:
# class Person():
class Person(object):
    # インスタンス生成時に実行されるメソッド(コンストラクタ)
    # 初期化時にインスタンスに値を保持させる
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run!' * num)

    # インスタンスが破壊されるときに実行されるメソッド(デストラクタ)
    def __del__(self):
        print('good bye')


person = Person('Mike')
person.say_something()

