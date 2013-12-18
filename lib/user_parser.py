# We are not using this parser, but leaving it here just for a reference.

## Parse the train file according to users.
#
## This was originally written by a Kaggler (Miroslaw Horbal, miroslaw@gmail.com) and presented on a discussion board:
# http://www.kaggle.com/c/yandex-personalized-web-search-challenge/forums/t/6489/python-code-for-parsing-data

__author__ = 'Yosuke Sugishita'
__email__ = 'yosuke.sugi@gmail.com'
__date__ = 'December 6, 2013'
 
def parse_users(file):
    """
    A generator that yields user objects from file
    
    Each user object has the following format
      {'UserID': int,
        'Sessions':[
          { SessionID: int,
            Day: int,
            Queries: [ { TimePassed: int,
                     SERPID: int,
                     QueryID: int,
                     ListOfTerms: [TermID_1, ...],
                     Clicks: [{ TimePassed: int, SERPID: int, URLID: int }, ...],
                     URL_DOMAIN: [(URLID_1, DomainID_1), ...] }, ...]
          }, ...
        ]
      }
    """
    ## Read the first line and get the first user_id (assuming this is metadata)
    s = {'UserID': None, 'Sessions': []}
    for line in file:
        sline = line.strip().split('\t')
        ## If this line is metadata ('M') and if it's a new user, yield s and create a new dictionary.
        # Assume there is at least one session associated with each user.
        if sline[1] == 'M' and s['Sessions'] and int(sline[3]) != current_user_id:
            yield s
            s = {'UserID': None, 'Sessions': []}
        if sline[1] == 'M':
            current_user_id = int(sline[3])
            s['UserID'] = current_user_id
            session_id, record_type, day = sline[:3]
            s['Sessions'].append( create_session(session_id, day) )
        elif sline[2] == 'Q': # 'Q' for Query
            session_id, time_passed, record_type, serpid, quid, terms = sline[:6]
            url_list = sline[6:]
            s['Sessions'][-1]['Queries'].append(create_query(time_passed, serpid, quid, terms, url_list))
        elif sline[2] == 'C': # 'C' for Click
            session_id, time_passed, record_type, serpid, urlid = sline
            s['Sessions'][-1]['Queries'][-1]['Clicks'].append(create_click(time_passed, serpid, urlid))
 
def create_session(session_id, day):
    return { 'SessionID': int(session_id),
              'Day': int(day),
              'Queries': [] }
 
def create_query(time_passed, serp_id, query_id, list_of_terms, url_list):
    return { 'TimePassed': int(time_passed),
              'SERPID': int(serp_id),
              'QueryID': int(query_id),
              'Clicks': [],
              'ListOfTerms': [int(t) for t in list_of_terms.split(',')],
              'URL_DOMAIN': [tuple(int(ui) for ui in u.split(','))
                                for u in url_list] }
 
def create_click(time_passed, serp_id, url_id):
    return { 'TimePassed': int(time_passed),
              'SERPID': int(serp_id),
              'URLID': int(url_id) }
