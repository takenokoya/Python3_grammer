# lambda
l = ['Mon', 'tue', 'Wed', "thu", 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()
sample_func = lambda word: word.capitalize()

change_words(l, sample_func)
print('#########')
# 以下は等価
change_words(l, lambda word: word.capitalize())
print('#########')
change_words(l, lambda word: word.lower())
print('#########')
