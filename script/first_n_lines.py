## Take first n lines from the 16GB train data and write them into a single file caled 'train_head'

# The number of lines to take:
n = 10**3 # There are about 160 million lines in the train file.

import os
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
data_dir = os.path.join(home_dir, "data")
train_data = open(os.path.join(data_dir, "train"), 'rb')
new_file_path = os.path.join(data_dir, "train_head")

with open(new_file_path, 'w') as f:
    for i in range(0, n):
        f.write(train_data.next())
