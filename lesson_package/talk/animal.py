from lesson_package.tools import utils


def sing():
    return 'jfksjfdkjkajfklasjfjdsajf'


def cry():
    return utils.say_twice('cryfjjskjfahsfjhashahkja')


# 他のファイルからimportしたときに実行されないようにする記述
if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)

