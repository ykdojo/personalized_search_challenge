# Attempt on a Kaggle competition, *Personalized Web Search Challenge* (hosted by Yandex)
URL: http://www.kaggle.com/c/yandex-personalized-web-search-challenge

## Deadline: Friday, January 10, 2014

## Team Members
- Yosuke Sugishita
- David Kim
- Possibly Brendan and David Hsiao
- Idea: Should we make this open to people in Data Science Club and local data meetups on Meetup.com?  If we have too many people (I think 4-5 people in one team is a limit), we can make multiple teams and still work together.

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
- Database?
  - Looks like some people on Kaggle tried to use databases, but it didn't work out very well:
  - http://www.kaggle.com/c/yandex-personalized-web-search-challenge/forums/t/6183/handling-703-000-000-urls/
  - http://www.kaggle.com/c/yandex-personalized-web-search-challenge/forums/t/6353/someone-else-using-r-mysql-as-database-need-some-feedback

## Notes on possible strategies (more on the wiki)
Two ways to look at this problem:
  1. Collaborative filtering (recommender) problem
    - Netflix Prize winners' solution: http://www2.research.att.com/~volinsky/papers/ieeecomputer.pdf
  2. We can also look at the past clicks a certain user has performed.
    - The user is probably more (or less) likely to click the pages they already clicked and liked. => Need to test this.

Our first strategy is based on 2.  (Low-hanging fruits! Yay!)
https://github.com/yosukesugishita/personalized_search_challenge/wiki/Initial-Model:-Take-advantage-of-multiple-visits

## Some notes on the data
#### The train file is big (16GB when uncompressed)

We need to think about how to handle this.  Perhaps use a database, like sqlite or MySQL?
I (Yosuke) suspect we can try our first strategies with a randomly-sampled subset of the data.  How would we go about it?

#### Train and test
In the competition, the first 27 days are used as train data, and the last 3 days as test data. (http://www.kaggle.com/c/yandex-personalized-web-search-challenge/data)

Perhaps we can locally test our model using the first 24 days train and the next 3 days as test.
