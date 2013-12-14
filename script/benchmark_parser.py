## This script benchmarks the time it takes to run parser.py
#  on the whole train file.

import os
import parser
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
# Use small data (head) for testing-- use first_n_lines.py
#train_data = open(home_dir + "/data/train_head", 'rb') # this one is the real data
train_data = open(home_dir + "/data/train", 'rb') # this one is the real data
session_generator = parser.parse_sessions(train_data)

count = 0
while True:
    try:
        # Print at every millionth session
        if count % (10 ** 6) == 0:
            print "...reading the {0}th session".format(count)
        # next() raises the StopIteration exeption when hitting the end
        session_generator.next()
        count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "Session count:", count
