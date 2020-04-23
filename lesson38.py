animal = 'cat'


def f():
    global animal
    animal = 'dog'
    print('local_scope:', animal)
    print('local:', locals())


f()

print('global_scope:', animal)
print('global:', locals())
