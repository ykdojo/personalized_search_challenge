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


### The following results are from the whole train file.
# mean: [ 0.65162438  0.21038608  0.13324812  0.09167282  0.06874233  0.05194465
#  0.04036323  0.0332495   0.02966097  0.03055541]
# length: 65172853

global_means = np.array([0.65629868,0.21159365,0.13479269,0.09191065,0.06907311,0.05177313,0.04077629,0.03368095,0.03000333,0.03060453])
num_queries = 638729 # length: 638729
num_hits = num_queries * 10
skipped_means = np.array([0.27838331,0.09804045,0.07216911,0.05031282,0.03849023,0.03009795,0.02436445,0.01956693,0.01893318,0.05848492])
# numbers of skipped urls that have been shown to users
skipped_lengths = np.array([16973,31691,32216,30529,29488,28075,26473,25400,22553,4343])
ratio_skipped = sum(skipped_lengths) / float(num_hits)

global_sums = global_means * num_queries
skipped_sums = skipped_means * skipped_lengths

# numbers of non-skipped urls
non_skipped_lengths = num_queries - skipped_lengths
non_skipped_means = (global_sums - skipped_sums) / non_skipped_lengths


print "ratio_skipped:", ratio_skipped
width = 0.2
ind = np.arange(1, 11)
plt.bar(ind, global_means, width, color='r')
plt.bar(ind+width, non_skipped_means, width, color='b')
plt.bar(ind+2*width, skipped_means, width, color='y')
# Plot shows global, non-skipped, and then skipped cases.
plt.show()