## Take first n lines from the 16GB train data and write them into a single file.
# The Kaggle's competition page shows the following statistic: (http://www.kaggle.com/c/yandex-personalized-web-search-challenge/data)
# > Unique queries: 21,073,569 
# This script splits the 'train' file into smaller files, each of which has a million lines.
n = 1000000#0 # There are about 160 million lines in the train file.

import os
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
data_dir = os.path.join(home_dir, "data")
train_data = open(os.path.join(data_dir, "train"), 'rb')

with open(os.path.join(data_dir, "train_small"), 'w') as f:
    for i in range(0, n):
        f.write(train_data.next())
