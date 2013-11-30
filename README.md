*** Attempt on a Kaggle competition, *Personalized Web Search Challenge* (hosted by Yandex)
URL: http://www.kaggle.com/c/yandex-personalized-web-search-challenge

** Deadline: Friday, January 10, 2014

** Team Members:
- Yosuke Sugishita
- David Kim
- (Possibly Brendan and David Hsiao)

** Some ideas on our team name:
- Asian Revolution
- West Coasters
- Canadian Kimchi Roll

** File structure:
- script
Contains our scripts.
- data
Contains all the data, like test and train.  Not committed due to the large size of the files.  Download them directly from Kaggle.

** Some notes on the data
- The train file is big (16GB when uncompressed)
So we need to think about how to handle this.  Perhaps use a database, like sqlite or MySQL?
I (Yosuke) suspect we can try our first strategies with a randomly-sampled subset of the data.  How would we go about it?

** Note on possible strategies
In the competition, the first 27 days are used as train data, and the last 3 days as test data. (http://www.kaggle.com/c/yandex-personalized-web-search-challenge/data)
So perhaps we can locally test our model using the first 24 days train and the next 3 days as test.