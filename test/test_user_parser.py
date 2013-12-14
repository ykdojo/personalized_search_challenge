## Informally test user_parser.py

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + "/script") # for importing functions

import user_parser

f = open(home_dir + '/data/train', 'rb')
sp = user_parser.parse_users(f)
users = [sp.next() for i in range(10)]

print "number of sessions for user[0]", len(users[0]['Sessions'])
print "number of sessions for user[1]", len(users[1]['Sessions'])
