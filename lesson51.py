# class継承
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'
                 ):
        # self.model = model と繰り返すのではなく、親クラスを呼び出してメソッド呼び出し
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # 読み込みしかできなくする(getter)
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # 書き込みを可能にする(setter)
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '123456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto_run')

car = Car()
car.run()
print('###########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('###########')
# passwdがあっているときだけ、enable_auto_runが書き込み可能となる
tesla_car = TeslaCar('Model S', passwd='123456')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
print('###########')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

