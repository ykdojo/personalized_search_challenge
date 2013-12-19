## This script compares the global means and skipped means for each rank position.
# The numbers are from CSV files in data/results
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

# Ignore the first three lines in CSV as they are comments
global_table = pd.read_csv(home_dir + '/data/results/global_means.csv', skiprows=3)
global_means = global_table['global_means']
global_lengths = global_table['global_lengths']

skipped_table = pd.read_csv(home_dir + '/data/results/skipped_means.csv', skiprows=3)
skipped_means = skipped_table['skipped_means']
skipped_lengths = skipped_table['skipped_lengths']

ratio_skipped = sum(skipped_lengths) / float(sum(global_lengths))

global_sums = global_means * global_lengths
skipped_sums = skipped_means * skipped_lengths

non_skipped_lengths = global_lengths - skipped_lengths
non_skipped_means = (global_sums - skipped_sums) / non_skipped_lengths

print "ratio_skipped:", ratio_skipped
width = 0.2
ind = np.arange(1, 11)
plt.bar(ind, global_means, width, color='r')
plt.bar(ind+width, non_skipped_means, width, color='b')
plt.bar(ind+2*width, skipped_means, width, color='y')
# Plot shows global, non-skipped, and then skipped cases.
plt.show()
