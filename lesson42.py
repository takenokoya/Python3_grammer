# fromを使ってutilsを呼びだす
from lesson_package import utils
# function だけを呼び出しも可能(ただし呼び出し元がわかりづらいので好まれない)
from lesson_package.utils import say_twice

r = utils.say_twice('hello')
print(r)
