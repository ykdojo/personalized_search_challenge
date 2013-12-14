## This file finds the global satisfaction mean in the training file.
# There are three types of relevance grades:
#
# 0 (irrelevant) grade corresponds to documents with no clicks and clicks with dwell time strictly less than 50 time units
# 1 (relevant) grade corresponds to documents with clicks and dwell time between 50 and 399 time units (inclusively)
# 2 (highly relevant) grade corresponds to the documents with clicks and dwell time not shorter than 400 time units. In addition, the relevance grade of 2 assigned to the documents associated with clicks which are the last actions in the corresponding sessions.


import parser


## <Pseudo-code>
# 1. Go through the lines of train file
# 2. Parse 
# 3. For each document, find the relevance grade
#    -> Add to a numpy array and get the mean!
