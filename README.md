# Attempt on a Kaggle competition, *Personalized Web Search Challenge* (hosted by Yandex)
URL: http://www.kaggle.com/c/yandex-personalized-web-search-challenge

## Deadline: Friday, January 10, 2014

## Team Members
- Yosuke Sugishita
- David Kim
- (Possibly Brendan and David Hsiao)

## Ideas on our team name
- Asian Revolution
- West Coasters
- Canadian Kimchi Roll

## File structure
- script
  - Contains our scripts.
- data
  - Contains all the data, like test and train.  Not committed due to the large size of the files.  Download them directly from Kaggle.

## About branches / pull requests
All the code must be reviewed by at least by one other person before being pulled into the master.  Make a branch, write code, test, and send a pull request.  Use short, descriptive names for branches.

*Never* directly work on the master.

## Tools
- Version Control
  - Git with scm_breeze (https://github.com/ndbroadbent/scm_breeze)
    - Note, scm_breeze is a must.  It's a huge productivity booster.
- Language(s)
  - Python
- Editors
  - Vim
  - PyCharm might be good.  The same company's Ruby IDE is awesome.
  - Any other editors you like?

## Some notes on the data
**The train file is big (16GB when uncompressed)**

So we need to think about how to handle this.  Perhaps use a database, like sqlite or MySQL?
I (Yosuke) suspect we can try our first strategies with a randomly-sampled subset of the data.  How would we go about it?

## Note on possible strategies
I (Yosuke) think there are two ways to look at this problem.
  1. Collaborative filtering (recommender) problem
    - Netflix Prize winners' solution: http://www2.research.att.com/~volinsky/papers/ieeecomputer.pdf
  2. We can also look at the past clicks a certain user has performed.
    - The user is probably more (or less) likely to click the pages they already clicked and liked. => Need to test this.

#### About data
In the competition, the first 27 days are used as train data, and the last 3 days as test data. (http://www.kaggle.com/c/yandex-personalized-web-search-challenge/data)

So perhaps we can locally test our model using the first 24 days train and the next 3 days as test.
