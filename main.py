import os
from os.path import abspath, join

for top_dir, directories, files in os.walk('.'):
    for directory in directories:
        print(abspath(join(top_dir, directory)))
    for _file in files:
        print(abspath(join(top_dir, _file)))
    break
