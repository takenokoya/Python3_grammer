# psycopg2からAWS RedshifへCOPYコマンドを実行するサンプルコード
import psycopg2
from datetime import datetime


# Redshift接続情報
hostName = "XXXXXXXXXXXXXXXXXXXXXXXXX"
databaseName = "XXXXXXX"
portNo = "5439"
userName = "XXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXXXXXX"

# Connectionオブジェクト作成
conn = psycopg2.connect(
    host=hostName,
    database=databaseName,
    port=portNo,
    user=userName,
    password=password
)
print("psycopg2 connected.")

# SQL文を実行するためにはConnectionオブジェクトからさらにCursorオブジェクトを作成
cur = conn.cursor()
print("psycopg2 cursor opened.")

# file名
today = datetime.now().strftime('%Y-%m-%d')
file = 's3://XXXXXXXX/XXXXXXXXXX_{}'.format(today)
# copy文
copy_statement = """
COPY XXXXXX.XXXXXXXX
FROM '{}'
credentials 'aws_iam_role=XXXXXXXXXXXXXXX'
gzip
delimiter ','
csv
ignoreheader 1
region 'ap-northeast-1'
""".format(file)

print(copy_statement)
# Cursorオブジェクトのexecute()メソッドでSQL文を実行
print('COPY start.')
cur.execute(copy_statement)
print('COPY end.')
# 変更をDBに保存
conn.commit()
# コネクションのクローズ
cur.close()
print("psycopg2 cursor closed.")
conn.close()
print("psycopg2 connection closed.")

