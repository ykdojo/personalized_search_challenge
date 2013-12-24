# Implementation of RankNET based on:
# http://research.microsoft.com/en-us/um/people/cburges/tech_reports/msr-tr-2010-82.pdf

from math import exp, log

_log = log # logarithmic function to be used
_exp = exp # exponential function to be used
    
# Indicates whether URL_i is actually more relevant
# than URL_j for a given query.Parameters are the
# actual relevance ratings for URLs i and j.
def indicator(relevance_i,relevance_j):
    if relevance_i > relevance_j:
        return 1
    elif relevance_i < relevance_j:
        return -1
    else:
        return 0  
          
# For a given query, each pair of urls U_i and U_j
# with feature vectors x_i and x_j is mapped to
# corresponding score values for U_i and U_j.
def score(self, x_i, x_j):
    pass #TODO: needs to be implemented
    
# Choice of this parameter determines the shape of
# the following sigmoid function.
shape = 1.0
# For a given query, for two given URLs: U_i and U_j,
# this is a sigmoid function that estimates the
# probability that U_i should be ranked higher than
# U_j based on their corresponding scores.
# This function is well-known in literature and has
# been shown to lead to good probability estimates.
def estimate(self, score_i, score_j):
    return (1 + _exp(-shape * (score_i - score_j))) ** -1

# This is the actual probability that URL U_i ranks
# higher than URL U_j, for a given query.
def actual(self, relevance_i, relevance_j):
    S_ij = indicator(relevance_i, relevance_j)
    return 0.5 * (1 + S_ij)

# Cross entropy cost between actual probability and
# our estimated probability.  Takes as parameters the
# actual and estimated probability for a given pair
# of urls U_i and U_j for a given query.
# This cost function penalizes the estimated distribution
# for deviating from the desired destribution.
def cost(self, actual, estimate):
    return (-actual * _log(estimate)) - ((1 - actual) * _log(1 - estimate))
        
        
    
    