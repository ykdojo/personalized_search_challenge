# This script finds the global relevance mean of all documents.

# It took 3 seconds to run on 100,000 lines (about 0.1%).  3 * 1000 = 3000 seconds = about 50 minutes?
# TODO: test on the whole file.

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

count = 0
relevance_rates = np.array([], np.int16)
while True:
    try:
        # Print at every millionth session
        if count % (10 ** 6) == 0:
            print "...reading the {0}th session".format(count)
        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()

        # Put relevance rate into the numpy array
        # Test by printing #TODO
        for query in session.queries:
            for click in query.clicks:
                relevance_rates = np.append( relevance_rates, click.satisfaction() )
        count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "\nSummary on relevance rates:"
print "mean:", np.mean(relevance_rates)
print "sd:", np.std(relevance_rates)
print "length:", len(relevance_rates)
