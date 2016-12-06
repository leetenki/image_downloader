import os
import numpy as np

categories = np.loadtxt('synset_words.txt', delimiter="\n", dtype=str)
for category in categories:
    category = category.split('\'')[1]
    dirname = category.split(' ')[0]
    keyword = ' '.join(category.split(' ')[1:])
    os.system('python download_image.py "%s" -d "1000_category/%s" -n %d' % (keyword, dirname, 5))
