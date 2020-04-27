class Person(object):
    def talk(self):
        print('talk')


class Car(object):
    def run(self):
        print('run')

# 多重継承
# 継承順は第一引数から優先
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

pcr = PersonCarRobot()
pcr.talk()
pcr.run()
pcr.fly()

