class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    # クラスメソッド
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.x)
print(a.what_is_your_kind())
# インスタンス生成してなくてもクラス変数にはアクセスできる
b = Person
print(b.kind)
# インスタンス生成していなくてもクラスメソッドは呼び出せる
print(b.what_is_your_kind())

Person.about(1997)