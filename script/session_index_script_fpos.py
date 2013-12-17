# Creates an index file with 3 columns - session id | start line | end line
# All columns are delimited by a tab symbol (\t)
# Each line corresponds to a session

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + os.sep + "script") # for importing functions

f = open(home_dir + os.sep + 'data' + os.sep + 'train', 'r')
session_index_file = open( home_dir + os.sep + 'data' + os.sep + 'session_index_file.txt', 'w')

previous_position = 0
last_line = 0

with f as file:
	for line in iter(file.readline,''):
		split_up = line.split('\t')
		if split_up[1] == 'M':
			# if this is a meta data line
			
			# write the end line
			if last_line!=0:
				session_index_file.write('\t' + str(last_line) + '\n')
				previous_position = last_line

			# write the session id + start line
			session_index_file.write(split_up[0] + '\t' + str(previous_position))
		last_line = file.tell()
	
	# handle case at eof
	session_index_file.write('\t' + str(file.tell()) + '\n')
