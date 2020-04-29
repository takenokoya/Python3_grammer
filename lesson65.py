import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

time = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(time)
print(time.isoformat())
print(time.strftime('%H%M%S%f'))

print(now)

# intervalを出したいとき
d = datetime.timedelta(weeks=1)
print(now + d)
print(now - d)

import time
print('###########')
# 2秒遅延してから
time.sleep(2)
print('###########')
print(time.time())

import os
import shutil

# バックアップファイル作成
file_name = 'test.txt'
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d')
    ))

with open(file_name, 'w') as f:
    f.write('test')
