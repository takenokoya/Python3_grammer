# 集合内for表記
s = set()

for i in range(10):
    s.add(i)

print(s)
print('###########')

# 以下でも同様の結果が得られる
s = {i for i in range(10)}
print(s)
print('###########')


