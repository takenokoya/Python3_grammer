# How to use ImportError
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

s = utils.say_twice('word')

print(s)
