# This is a module with functions to calculate DCG, iDCG, and nDCG.
# Kaggle page on DCG: https://www.kaggle.com/wiki/NormalizedDiscountedCumulativeGain

import math

# TODO: test these functions as they have not been rigorously tested.
# Input: relevance scores in a python list
# Output: dcg in float
def DCG(relevances):
	assert len(relevances) == 10
	dcg = 0
	
	for i in range(0, 10):
		dcg += ( pow(2, relevances[i]) - 1 ) / math.log(i + 2, 2)
	
	return dcg

# iDCG: the maximum possible value of DCG given the set of relevances
def iDCG(relevances):
	sorted_relevances = sorted(relevances, reverse=True)
	return DCG(sorted_relevances)

# normalized NDCG
def nDCG(relevances):
	return DCG(relevances) / iDCG(relevances)
