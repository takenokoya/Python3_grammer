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