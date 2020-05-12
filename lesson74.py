# psycopg2からPostgreSQLへ接続
import psycopg2
from datetime import datetime, timedelta

yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

# ログファイル
log_file = '/Users/sakaguchitakuya/PycharmProjects/python_programming/copy_log/log_{}'.format(yesterday)


def create_log(string):
    with open(log_file, 'w') as f:
        f.write(string + '\n')


def add_log(string):
    with open(log_file, 'a') as f:
        f.write(string + '\n')


# Redshift接続情報
hostName = "XXXXXXXXXXXXXXXXXXXXX"
databaseName = "XXXXXXXXXXXXXXXX"
portNo = "5439"
userName = "XXXXXXXXXX"
password = "XXXXXXXXXXXXXXXXXXXX"

# Connectionオブジェクト作成
conn = psycopg2.connect(
    host=hostName,
    database=databaseName,
    port=portNo,
    user=userName,
    password=password
)
create_log('psycopg2 connected')

# SQL文を実行するためにはConnectionオブジェクトからさらにCursorオブジェクトを作成
cur = conn.cursor()
add_log('psycopg2 cursor opened.')

# s3にあるcsvファイル
file = 's3://XXXXXXXXXXXXXXXXX_{}'.format(yesterday)
# copy文
copy_statement = """
copy XXXXXXXXXXXXXXXX
FROM '{}'
credentials 'aws_iam_role=xxxxxxxxxxxxxxxxx'
gzip
delimiter ','
csv
ignoreheader 1
region 'ap-northeast-1';

""".format(file)
add_log(copy_statement)

# Cursorオブジェクトのexecute()メソッドでSQL文を実行
add_log('COPY start.')
cur.execute(copy_statement)
add_log('COPY end.')
# 変更をDBに保存
conn.commit()
# コネクションのクローズ
cur.close()
add_log('psycopg2 cursor closed')
conn.close()
add_log('psycopg2 connection closed.')
