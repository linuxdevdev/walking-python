import os
from os.path import abspath, join, getsize

sizes = {}

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        #break

sorted_reults = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_reults[:10]:
    print("Path: {0}, size: {1}".format(path, sizes[path]))
    