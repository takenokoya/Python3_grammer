# Pythin3では以下の記述でもOK
# class Person:
# class Person():
class Person(object):
    def say_something(self):
        print('hello')


person = Person()
person.say_something()

