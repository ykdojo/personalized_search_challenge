# This script finds the global relevance mean of all documents for each rank.
# It returns means and plots them against rank (position) 

import matplotlib.pyplot as plt
import os
import sys
import numpy as np
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))

sys.path.insert(0, home_dir + "/script") # for importing functions
import session_parser as sp

# For testing
train_path = home_dir + '/data/train_head'
# For real
# train_path = home_dir + '/data/train'

session_generator = sp.parse_from_file(train_path)

session_count = 0
relevance_rates = list()

# sums for each rank, 1 up to 10
sums = np.zeros(10, dtype=int)
# counts all the queries
num_queries = 0

while True:
    try:
        # Print at every millionth session
        if session_count % (10 ** 6) == 0:
            print "...reading the {0}th session".format(session_count)
        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()

        # Put relevance rate into the numpy array
        for query in session.queries:
            num_queries += 1
            relevance_dict = query.url_pertinence()
            for i in range(0,10):
                url = query.hits[i][0] # query.hits[i] is a tuple like: (url, domain)
                sums[i] += relevance_dict[url]
        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

means = sums / float(num_queries)
print "\nSummary on relevance rates:"
print "mean:", means
print "length:", num_queries
plt.plot(means)
plt.show()
