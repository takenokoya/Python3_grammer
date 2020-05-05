# pandas を使ったサンプルコード

import pandas as pd


x = [('Gauss', 1777),
     ('Pascal', 1623),
     ('Turing', 1912),
     ('Bernoulli', 1700),
     ('Fourier', 1768),
     ('Maxwell', 1831)]
df = pd.DataFrame(data=x, columns=['Name', 'BirthYear'])
print(df)
# Dataframeクラスを使って合計や平均など様々な値を算出
print(df['BirthYear'].sum())
print(df['BirthYear'].mean())
# sqlっぽく絞り込み
print(df.query('BirthYear < 1800'))

