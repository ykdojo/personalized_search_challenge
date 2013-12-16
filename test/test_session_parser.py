## Informally test session_parser.py

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + "/script") # for importing functions

import session_parser as sp

gl = sp.generator_of_lists(home_dir + '/data/train_head')
#f = open(home_dir + '/data/train', 'rb')
session_generator = sp.parse(gl)
sessions = [session_generator.next() for i in range(10)]


#print "number of sessions for user[0]", len(users[0]['Sessions'])
#print "number of sessions for user[1]", len(users[1]['Sessions'])
