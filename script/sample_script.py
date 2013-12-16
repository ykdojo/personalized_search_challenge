#This is the script that creates a new file "sample" containing a random 1% sample of users from
#the original train data.
#
#Tested by running the script and confirming the output visually.
#

import random

random.seed(1)
sample_list = random.sample(xrange(5736333), int(5736333*0.01))
sample_dict = {}
for i in range(0, int(5736333*0.01)):
	sample_dict[sample_list[i]] = i;

file = open('train', 'r')
sample_file = open('sample', 'w')

typed = False;

for line in file:
	if 'M' in line:
		arr = line.split()
		if int(arr[3]) in sample_dict:
			typed = True;
			sample_file.write(line)
		else:
			typed = False;
	elif typed == True:
		sample_file.write(line)