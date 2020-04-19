# in, not in
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2
# OK
if not a == b:
    print('Not Equal')
# better
if a != b:
    print('Not Equal')

# boolean
is_ok = True
if is_ok:
    print("Hello")
