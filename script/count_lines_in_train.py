## Count the number of lines in the train file.
#
# It's useful for later deveopment, and this file can be
#  used as a template for traversing all the lines in the
#  train file.
#
# In Unix, one can use the following command to benchmark
#  the time it takes to run this program.
#  > time python count_lins_in_train.py
#
# Question: How about in Windows?
#
##===RESULT===
# The number of lines in the train file was: 164,439,537
# It took about 1 minute on my 8GB MacBook Pro to run this.



import os
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
data_dir = os.path.join(home_dir, "data")
# Use small data (head) for testing-- use first_n_lines.py
# train_data = open(os.path.join(data_dir, "train_head"), 'rb')
train_data = open(os.path.join(data_dir, "train"), 'rb') # this one is the real data

count = 0
while True:
    try:
        # Print at every 10-millionth line
        if count % (10 ** 7) == 0:
            print "...reading the {0}th line".format(count)
        # next() raises the StopIteration exeption when hitting the end
        train_data.next()
        count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "The number of lines in the train file was:", count
