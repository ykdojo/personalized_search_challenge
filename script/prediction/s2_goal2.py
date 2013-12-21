# This script makes predictions for the the test queries (strategy 2)
# with regards to the number of times a document has been previously skipped.

import os
import sys

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

sys.path.insert(0, home_dir + "/lib") # for importing functions
import session_parser as sp

test_path = home_dir + '/data/test' # for real
session_generator = sp.parse_from_file(test_path)

# Read results for times-skipped relevance means.
# Ignore the first 5 lines in CSV as they are comments.
ts_means = []
with open(home_dir + '/data/results/times_skipped.csv','r') as _input:
    for line in _input:
        line = line.strip()
        line = line.split(",")
        ts_means.append(line[0:len(line)-1]) # removes trailing comma

# File for writing our predictions
results = open(home_dir + '/data/prediction/s2_goal2.csv','w')
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
                    # Get the number of times this document was skipped
                    times_skipped = session.num_skipped(query, url_domain)
                    if times_skipped > 2:
                        pred[url] = 0.0
                    else:
                        pred[url] = ts_means[j][times_skipped]  
        # Rank url's according to our predictions
        # reverse=True because this needs to be in descending order
        pred_sorted = sorted(pred.iterkeys(), key=lambda x:pred[x], reverse=True) 
        # Write predictions to file
        for val in pred_sorted:
            results.write(str(session.sid)+","+str(val)+"\n")

        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

# Close file
results.close()
