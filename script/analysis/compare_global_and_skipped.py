## This script compares the global means and skipped means for each rank position.
# The numbers will be hard-coded here.
import numpy as np
import matplotlib.pyplot as plt

### The following results are from 1% sample.
# TODO: replace the following results with real results from 100% train.

## Results, global case
# Summary on relevance rates:
# mean: [ 0.65629868  0.21159365  0.13479269  0.09191065  0.06907311  0.05177313
#  0.04077629  0.03368095  0.03000333  0.03060453]
# length: 638729

## Results, skipped case
# Sums:  [ 4725  3107  2325  1536  1135   845   645   497   427   254]
# Lengths:  [ 16973  31691  32216  30529  29488  28075  26473  25400  22553   4343]
# Means:  [ 0.27838331  0.09804045  0.07216911  0.05031282  0.03849023  0.03009795
#  0.02436445  0.01956693  0.01893318  0.05848492]

global_means = np.array([0.65629868,0.21159365,0.13479269,0.09191065,0.06907311,0.05177313,0.04077629,0.03368095,0.03000333,0.03060453])
num_queries = 638729 # length: 638729
num_hits = num_queries * 10
skipped_means = np.array([0.27838331,0.09804045,0.07216911,0.05031282,0.03849023,0.03009795,0.02436445,0.01956693,0.01893318,0.05848492])
skipped_lengths = np.array([16973,31691,32216,30529,29488,28075,26473,25400,22553,4343])
ratio_skipped = sum(skipped_lengths) / float(num_hits)

print "ratio_skipped:", ratio_skipped
width = 0.2
ind = np.arange(1, 11)
plt.bar(ind, global_means, width, color='r')
plt.bar(ind+width, skipped_means, width)
plt.show()