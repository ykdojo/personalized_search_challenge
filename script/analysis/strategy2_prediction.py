# This script makes predictions for the the test queries (strategy 2)
# with regards to whether a document has been previously skipped. 
# Note: it doesn't (yet) consider the number of times a document has
# been skipped.

import os
import sys
import pandas as pd

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

sys.path.insert(0, home_dir + "/lib") # for importing functions
import session_parser as sp

test_path = home_dir + '/data/test'
session_generator = sp.parse_from_file(test_path)

# Read results for skipped and global versions
skipped_means = pd.read_csv(home_dir + '/data/results/skipped_means.csv',\
    sep=",", skipinitialspace=True, header='infer').skipped_means
global_means = pd.read_csv(home_dir + '/data/results/global_means.csv',\
    sep=",", skipinitialspace=True, header='infer').global_means

# File for writing our predictions
results = open(home_dir + '/data/predictions','w')
results.write("SessionID,URLID\n")

session_count = 0
while True:
    try:
        # Print at every millionth session
        if session_count % (10 ** 4) == 0:
            print "...reading the {0}th session".format(session_count)
        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()
        
        # Dictionary to store prediction values
        pred = dict()
        for query in session.queries:  
            if query.is_test: 
                for j in range(0,10):
                    url_domain = query.hits[j]
                    url = url_domain[0]
                    if session.was_skipped(query, url_domain): 
                        # use skipped version
                        pred[url] = skipped_means[j]
                    else: 
                        # use global version
                        pred[url] = global_means[j]   
        # Rank url's according to our predictions
        pred = sorted(pred.iterkeys(), key=lambda x:pred[x])
        # Write predictions to file
        for val in pred:
            results.write(str(session.sid)+","+str(val)+"\n")
             
        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break
    
# Close file
results.close()
