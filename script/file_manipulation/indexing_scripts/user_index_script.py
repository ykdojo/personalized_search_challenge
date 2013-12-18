# Creates an index file with 4 columns - user id | start line | end line | sessions by this user (comma delimited)
# All columns are delimited by a tab symbol (\t)
# Each line corresponds to a user

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(this_file_path))))
sys.path.insert(0, home_dir + os.sep + "script") # for importing functions

file = open(home_dir + os.sep + 'data' + os.sep + 'train', 'r')
user_index_file = open( home_dir + os.sep + 'data' + os.sep + 'user_index_file.txt', 'w')

previous_user = -1
line_counter = 0
sessions = list()

for line in file:
	split_up = line.split('\t')
	if split_up[1] == 'M':
		# if this is a meta data line
		sessions.append(split_up[0])
		if previous_user!=split_up[3]:
			# if we haven't come across a new user's meta data
			sessions.pop()
			previous_user = split_up[3]
			
			# write the end line number + sessions
			if line_counter != 0:
				user_index_file.write('\t' + str(line_counter-1) + '\t' + ','.join(sessions) + '\n')
			
			# write the user id + start line
			user_index_file.write(split_up[3] + '\t' + str(line_counter))
			
			# create new sessions list
			sessions = list()
			sessions.append(split_up[0])
	line_counter += 1

# handle case at eof
user_index_file.write('\t' + str(line_counter-1) + '\t' + ','.join(sessions) +'\n')