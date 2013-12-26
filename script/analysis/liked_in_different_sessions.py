# This script finds the mean relevance rate for each rank position,
# in the case the user has liked the same query-document pair at least once before.
#
# Look at query-document pairs users have liked in past sessions.

# <Pseudo-code>
## (in User class)
# returns the dictionary of query-url pair that are rated 2.
#   the form is: {(query_1, url_4): session_1, session_3, session_4, (query_2, url_3): session1}
# the sessions are the ones in which each query-url pair has been rated 2.
def get_queries_rated_2(self):
    # if we already have this in the object, return it.
    if not queries_rated_2 == None:
        return queries_rated_2
    # otherwise, compute it
    else:
        # find and set queries_rated_2

# returns the number of times the user has liked the same query-document pair
# in past sessions
def num_times_rated_2(self, query, url):
    # use get_queries_rated_2 for this



for each user:
    for each query:
        for each document:
            if document.times_liked_in_past_sessions:
                # Add this to the sum
            else:
                # Do something
