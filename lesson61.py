import tarfile

# tarファイルで圧縮
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir')
# tarファイルを展開
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     tr.extractall(path='test_tar')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())

