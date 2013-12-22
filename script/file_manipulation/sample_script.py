## This is the script that creates a new file "train_sample_p_percent_seed_s"
# containing a random p% sample of users from the original train data with the seed s.
#
## This script takes two arguments.
# > sample_script.py percentage seed
# for now, seed must be an integer.
#
# Takes around 3 minutes to run this on the whole train file.
# Tested by running the script and confirming the output visually.
import sys
import random
import os

# argv[0] is the file name, followed by real arguments
SAMPLE_PERCENTAGE = float(sys.argv[1])
SEED = int(sys.argv[2])


# Not sure if this file name would work with a decimal.
#original_filename = 'train_head_10k' # test with a header file
original_filename = 'train' # for real
output_filename = original_filename + '_sample_' + str(SAMPLE_PERCENTAGE) + '_percent_seed_' + str(SEED)

sample_ratio = SAMPLE_PERCENTAGE * 0.01 # convert from percentage to ratio

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

# Looked at the last line of train to find the last user ID
LAST_USER_ID = 5794359
# Kaggle provides the following information here: http://www.kaggle.com/c/yandex-personalized-web-search-challenge/data
NUM_UNIQUE_USERS = 5736333 # we won't use this constant, but keep it just for a reference
# Assuming that the train file is already sorted by user in an ascending order,
# 5736333 / 5794359 < 99%.  More than 1% of the user ID's are missing.

## Sample users.  If we uniformlly take 1% sample, for instance, from the
# whole user_id space, it's equivalent as taking 1% sample from all the 
# users, no matter how sparse the user_id space is.
# We won't necessarily exactly get 1% users, but we'll get a very close number.
#
# xrange(n) does not include n.
# for instance, xrange(3) == [0,1,2]
random.seed(SEED)
sample_list = random.sample( xrange(LAST_USER_ID + 1), int( (LAST_USER_ID + 1) * sample_ratio )) 
sample_dict = {}

# TODO: Put all the rest into a function that takes
# a list of user id's as input and outputs a sample file.
# That way, we will be able to test it more easily.
for user_id in sample_list:
	sample_dict[user_id] = True;

file = open(home_dir + os.sep + 'data' + os.sep + original_filename, 'r')
sample_file = open( home_dir + os.sep + 'data' + os.sep + output_filename, 'w')

typed = False;

for line in file:
	if 'M' in line:
		arr = line.split()
		if int(arr[3]) in sample_dict:
			typed = True;
			sample_file.write(line)
		else:
			typed = False;
	elif typed == True:
		sample_file.write(line)
