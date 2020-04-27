class Person(object):
    # クラス変数
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

# リストが共有されるケース
# クラス変数としてリストを初期化した場合は、別のインスタンスからの呼び出しでもリストが共有される
# リストを共有しないように__init__でインスタンス毎にリストを初期化するとよい
class T(object):
    # words = []
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')
print(c.words)
print(d.words)