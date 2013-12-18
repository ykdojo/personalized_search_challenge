#This script calculates the count of urls repeated once, twice, thrice, ... (globally)

import matplotlib.pyplot as plt
import os
import sys
import numpy as np

final_dict1 = {}
final_dict2 = {}
final = [final_dict1, final_dict2]

def queryParse(queries):
    # finds any URLs repeated in the given session
    urls = []
    domains = []
    for query in queries:
        for hit in query.hits:
            urls.append(hit[0])
            domains.append(hit[1])
    d1 = {x:urls.count(x) for x in urls}
    d2 = {x:domains.count(x) for x in domains}
    d = [d1,d2]
    for j in range(0,2):
        frq = d[j].values()
        dict = {x:frq.count(x) for x in frq} # key = frequency, val = count of occurrences
        findict = final[j]
        for key in dict:
            if key in findict:
                findict[key] += dict[key]
            else:
                findict[key] = dict[key]



this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))

sys.path.insert(0, home_dir + "/script") # for importing functions
import session_parser as sp

train_path = home_dir + '/data/train_sample'
session_generator = sp.parse_from_file(train_path)

session_count = 0

while True:
    try:
        # Print at every millionth session
        if session_count % (10 ** 6) == 0:
            print "...reading the {0}th session".format(session_count)

        # next() raises the StopIteration exeption when hitting the end
        session = session_generator.next()

        queryParse(session.queries)

        session_count += 1
    except StopIteration as e:
        print "Reached the end of the file."
        break

print "Urls: ",final[0]
plt.plot(final[0].keys(),final[0].values())
plt.show()

print "Domains: ",final[1]
plt.plot(final[1].keys(),final[1].values())
plt.show()