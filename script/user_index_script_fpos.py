# Creates an index file with 4 columns - user id | file start position | end position | sessions by this user (comma delimited)
# All columns are delimited by a tab symbol (\t)
# Each line corresponds to a user

# Example of how to get relevant lines for an entry 
# f = open('user_index_file2.txt','r')
# f.seek(file start position, 0) <- ALWAYS RELATIVE TO ZERO!
# while(f.tell() < file end position):
# 	print f.readline()
# This will open the file, go to position required, and while we haven't reached the end position,
# continue to print out files.

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + os.sep + "script") # for importing functions

f = open(home_dir + os.sep + 'data' + os.sep + 'train', 'r')
user_index_file = open( home_dir + os.sep + 'data' + os.sep + 'user_index_file2.txt', 'w')

previous_user = -1
previous_position = 0
last_line = 0 
sessions = list()

with f as file:
	for line in iter(file.readline,''):
		split_up = line.split('\t')
		if split_up[1] == 'M':
			# if this is a meta data line
			sessions.append(split_up[0])
			if previous_user!=split_up[3]:
				# if we haven't come across a new user's meta data
				sessions.pop()
				previous_user = split_up[3]
			
				# write the end line number + sessions
				if last_line != 0:
					user_index_file.write('\t' + str(last_line) + '\t' + ','.join(sessions) + '\n')
					previous_position = last_line

				# write the user id + start line
				user_index_file.write(split_up[3] + '\t' + str(previous_position))
				
				# create new sessions list
				sessions = list()
				sessions.append(split_up[0])
		last_line = file.tell()

# handle case at eof
user_index_file.write('\t' + str(file.tell()) + '\t' + ','.join(sessions) +'\n')
