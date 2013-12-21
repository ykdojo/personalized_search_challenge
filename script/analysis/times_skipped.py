# This script finds the mean relevance rate of documents classified by the
# number of times they have been skipped.

# Note: If a document is skipped 0 times, then it is possible that it never 
# appeared in previous queries, or that it appeared and was clicked, or that
# it was missed in previous queries.

import os
import sys
import numpy as np

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

sys.path.insert(0, home_dir + "/lib") # for importing functions
import session_parser as sp

# For testing
#train_path = home_dir + '/data/train_head_10k'
#train_path = home_dir + '/data/train_head_million'
train_path = home_dir + '/data/train_sample_10k'

# For real
#train_path = home_dir + '/data/train'
session_generator = sp.parse_from_file(train_path)

session_count = 0

# Skips greater than or equal to this value will be aggregated
limit = 3
# 2D array stores the sums for each position for each 'number of skips'
counts = [np.zeros(limit+1,dtype=int) for i in range(10)]
# 2D array stores the corresponding lengths
lengths = [np.zeros(limit+1,dtype=int) for i in range(10)]

while True:
    try:
        # Print at every millionth session
        if session_count % (10 ** 6) == 0:
            print "...reading the {0}th session".format(session_count)

        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()

        # adds skipped document relevance rates to array
        for query in session.queries:  
            relevance_dict = query.url_pertinence()
            for j in range(0,10):
                url_domain = query.hits[j]
                # Get number of times this document was previously skipped within session
                times_skipped = session.num_skipped(query, url_domain)
                if times_skipped >= limit: #if time_skipped > 2
                    counts[j][limit] += relevance_dict[url_domain[0]]
                    lengths[j][limit] += 1
                else: 
                    counts[j][times_skipped] += relevance_dict[url_domain[0]]
                    lengths[j][times_skipped] += 1
        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

means = []
for i in range(10):
    means.append((counts[i]) / (lengths[i]).astype(float))     
    
output = open(home_dir + '/data/results/times_skipped_test.csv','w')

#output.write("#Note: NaN and zero are not the same\n")
#output.write("#NaN = no such value exists\n")
#output.write("#Zero = Relevance mean is zero\n\n")
#output.write("MEANS:\n")
for i in range(10):
    output.write(str(means[i][0]))
    for j in range(1,len(means[i])):
        output.write(",")
        output.write(str(means[i][j]))        
    output.write("\n")
"""
output.write("\nLENGTHS:\n")
for i in range(10):
    for j in range(len(means[i])):
        output.write(str(lengths[i][j]))
        output.write(",")
    output.write("\n")
"""
output.close()