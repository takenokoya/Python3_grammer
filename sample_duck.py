def animal_ability(animal):
    animal.voice()
    animal.walking()


class Duck():
    def voice(self):
        print('gua! gua!')

    def walking(self):
        print('walk with oshiri furi furi')

class Elephant():
    def voice(self):
        print('paooooooorn!')

    def walking(self):
        print('walk with pao pao')

class Hourse():
    def voice(self):
        print('hi, hiiiiiiirn!')

    def walking(self):
        print('walk with pakara pakara')

duck = Duck()
elephant = Elephant()
hourse = Hourse()

animal_ability(duck)
print('#########')
animal_ability(hourse)
print('#########')
animal_ability(elephant)



