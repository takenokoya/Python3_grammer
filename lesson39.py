# error handling
l = [1, 2, 3]
i = 5

try:
    l[i]
    # () + l
except IndexError as e:
    print("Don't warry: {}".format(e))
except NameError as e:
    print('Name Error:', e)
except Exception as e:
    print('Other', e)
else:
    print('done')
finally:
    print('clean up')

# exceptでエラーを捕捉
# elseはエラーがなかったときに実行される
# finallyはエラーがあっても必ず最後に実行される
