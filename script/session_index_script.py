# Creates an index file with 3 columns - session id | start line | end line
# All columns are delimited by a tab symbol (\t)
# Each line corresponds to a session

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + os.sep + "script") # for importing functions

file = open(home_dir + os.sep + 'data' + os.sep + 'train', 'r')
session_index_file = open( home_dir + os.sep + 'data' + os.sep + 'session_index_file.txt', 'w')

line_counter = 0

for line in file:
	split_up = line.split('\t')
	if split_up[1] == 'M':
		# if this is a meta data line
		
		# write the end line
		if line_counter != 0:
			session_index_file.write('\t' + str(line_counter-1) + '\n')
		
		# write the session id + start line
		session_index_file.write(split_up[0] + '\t' + str(line_counter))
	line_counter += 1

# handle case at eof
session_index_file.write('\t' + str(line_counter-1) + '\n')