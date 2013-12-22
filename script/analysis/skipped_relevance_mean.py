## This script finds the relevant means for each document position where
# documents have been skipped within a session.
#
## At the same time, it will find the non-skipped case (global case)

# Took 52 seconds to run on 0.6% of the train file.
# -> 52 / 0.6% ~= 9000 = 150 minutes.
# Should take around 150 minutes to run on the whole train file.

import matplotlib.pyplot as plt
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
train_path = home_dir + '/data/train_sample_100k'

# For real
train_path = home_dir + '/data/train'

session_generator = sp.parse_from_file(train_path)

session_count = 0
relevance_rates = list()

# sums for each skipped document (positions 1 to 10)
sums_skipped = np.zeros(10, dtype=int)
# array that stores the count for each skipped document (positions 1 to 10)
num_skipped = np.zeros(10, dtype=int)

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
                if session.was_skipped(query, url_domain): 
                    sums_skipped[j] += relevance_dict[url_domain[0]]
                    num_skipped[j] += 1
        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "sums_skipped: ",sums_skipped
print "Lengths: ",num_skipped

means_skipped = sums_skipped / num_skipped.astype(float)

print "Means: ",means

plt.bar(range(1,11),means)
plt.show()
