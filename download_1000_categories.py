import os
import numpy as np

base_dirname = '1000_categories'
if not os.path.exists(base_dirname):
    print('create directory %s/' % base_dirname)
    os.mkdir(base_dirname)

categories = np.loadtxt('synset_words.txt', delimiter="\n", dtype=str)
for category in categories:
    category = category.split('\'')[1]
    dirname = category.split(' ')[0]
    keyword = ' '.join(category.split(' ')[1:])
    os.system('python download_image.py "%s" -d "%s/%s" -n %d' % (keyword, base_dirname, dirname, 1))
