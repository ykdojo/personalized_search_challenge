## Oops.
# I just found out that I could've used the following line in unix:
# > head -n 1000 train > train_head
# > tail -n 1000 train > tarin_tail


## Assumption: The user ID goes from 0 to 5,736,332 (there are 5,736,333 unique users).
# In order to test this, take last n lines from train data and write them into a single file caled 'train_tail'
#  (I already checked the first several ID's, and the assumption holds)
#
#===<RESULT>====
#   The last ID was 5,794,359.  So there are about 50,000 missing ID's.
#   It's about 1%, so not too bad (We can still use this as an index for random samples).

# <Pre-experiment>
# I did a little experiment, and found that the first 10 lines contain 878 bytes.
# -> Go to the (n * 100)th position from the end using file.seek(), and get the rest of the lines.
#     This is not an exact method, but good enough for the purpose.
# I chose to use this method because it takes a lot of time to go through the whole file.

# The number of lines to take:
n = 10**3 # There are about 160 million lines in the train file.

import os
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))
data_dir = os.path.join(home_dir, "data")
train_data = open(os.path.join(data_dir, "train"), 'rb')
new_file_path = os.path.join(data_dir, "train_tail")

train_data.seek(-n * 100, 2)
lines = train_data.readlines()
with open(new_file_path, 'w') as f:
    for line in lines:
        f.write(line)
