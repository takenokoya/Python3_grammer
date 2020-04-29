# zipファイル
import zipfile
import glob

# with zipfile.ZipFile('test.zip', 'w') as z:
#     z.write('test_dir')
#     z.write('test_dir/test.txt')

# フォルダ内を再帰的に探して実行
# with zipfile.ZipFile('test.zip', 'w') as z:
#     for f in glob.glob('test_dir/**', recursive=True):
#         print(f)
#         z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')
    with z.open('test_dir/test.txt') as f:
        print(f.read())


