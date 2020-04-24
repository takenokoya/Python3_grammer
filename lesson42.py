# fromを使ってutilsを呼びだす
from lesson_package.tools import utils

# function だけを呼び出しも可能(ただし呼び出し元がわかりづらいので好まれない)

r = utils.say_twice('hello')
print(r)
