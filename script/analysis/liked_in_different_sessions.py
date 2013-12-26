# This script finds the mean relevance rate for each rank position,
# in the case the user has liked the same query-document pair at least once before.
#
# Look at query-document pairs users have liked in past sessions.

# <Pseudo-code>

# (in User class)
# returns the number of times the user has liked the same query-document pair
# in past sessions
def times_liked_in_past_sessions(self, query, document):
    get all the past queries
    get the ones that are the same as the given query
    


for each user:
    for each query:
        for each document:
            if document.times_liked_in_past_sessions:
                # Add this to the sum
            else:
                # Do something
