# This script finds the mean relevance rate for each rank position,
# in the case the user has liked the same query-document pair at least once before.
#
# Look at query-document pairs users have liked in past sessions.

# <Pseudo-code>
for each user:
    for each query:
        for each document:
            if document.times_liked_in_past_sessions > 0:
                # Add this to the sum
            else:
                # Do something
