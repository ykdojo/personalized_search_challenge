## Informally test session_parser.py

import os
import sys
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + "/script") # for importing functions

import session_parser as sp

session_generator = sp.parse_from_file(home_dir + '/data/train_head')
sessions = [session_generator.next() for i in range(10)]

print sessions[0].queries[0].clicks
