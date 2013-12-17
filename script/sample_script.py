#This is the script that creates a new file "sample" containing a random 1% sample of users from
#the original train data.
#
#Tested by running the script and confirming the output visually.
#

import random
import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + os.sep + "script") # for importing functions

UNIQUE_USERS = 5736333

random.seed(1)
sample_list = random.sample(xrange(UNIQUE_USERS), int(UNIQUE_USERS*0.01))
sample_dict = {}
for user_id in sample_list:
	sample_dict[user_id] = True;

file = open(home_dir + os.sep + 'data' + os.sep + 'train', 'r')
sample_file = open( home_dir + os.sep + 'data' + os.sep + 'train_sample', 'w')

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