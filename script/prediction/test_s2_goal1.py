## This script tests s2_goal1.py locally.
TEST_FILE_NAME = 'train_sample_1_percent_seed_2'

import os
import sys
import pandas as pd

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

sys.path.insert(0, home_dir + "/lib") # for importing functions
import session_parser as sp

test_path = home_dir + '/data/' + TEST_FILE_NAME
session_generator = sp.parse_from_file(test_path)

# Read results for skipped and global versions
# Ignore the first 3 lines in CSV as they are comments.
skipped_means = pd.read_csv(home_dir + '/data/results/skipped_means.csv',\
    sep=",", skipinitialspace=True, header='infer', skiprows=3).skipped_means
global_means = pd.read_csv(home_dir + '/data/results/global_means.csv',\
    sep=",", skipinitialspace=True, header='infer', skiprows=3).global_means


# Go through each session
session_count = 0
count_changed = 0 # counts the number of ranks that have been changed
sum_ndcg_from_pred = 0
sum_ndcg_baseline = 0
query_count = 0 # counts the number of queries

while True:
    try:
        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()
        
        # TODO: Perhaps put the following part in a function or something
        for query in session.queries:  
            query_count += 1
            pred = dict() # dictionary to store prediction values
            # Pretend all the queries are test queries in the test file.
            # if query.is_test: 
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
            # reverse=True because this needs to be in descending order
            pred_sorted = sorted(pred.iterkeys(), key=lambda x:pred[x], reverse=True) 
            sum_ndcg_from_pred += query.ndcg_from_pred(pred_sorted)
            sum_ndcg_baseline += query.ndcg_baseline()
            # count the number of ranks that have been changed
            if list(query.urls()) == pred_sorted:
                count_changed += 1

        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "Number of queries tested:", query_count
print "Number of queries for which the ranking has been changed:", count_changed
print "mean nDCG, baseline:", sum_ndcg_baseline / query_count
print "mean nDCG, from prediction", sum_ndcg_from_pred / query_count
