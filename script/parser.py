## This was originally written by a Kaggler and presented on a discussion board:
# http://www.kaggle.com/c/yandex-personalized-web-search-challenge/forums/t/6489/python-code-for-parsing-data

__author__ = 'Miroslaw Horbal'
__email__ = 'miroslaw@gmail.com'
__date__ = 'December 1, 2013'
 
# Notes
# Dec 2, 2013: Updated the parser to fix the bug noticed by kinnskogr
#              on the kaggle forums. The fix involves directly assigning
#              clicks to query objects
 
def parse_sessions(file):
    """
    A generator that yields session objects from file
    
    Each session object has the form:
        { SessionID: int,
          Day: int,
          USERID: int,
          Queries: [ { TimePassed: int,
                   SERPID: int,
                   QueryID: int,
                   ListOfTerms: [TermID_1, ...],
                   Clicks: [{ TimePassed: int, SERPID: int, URLID: int }, ...],
                   URL_DOMAIN: [(URLID_1, DomainID_1), ...] }, ...]
        }
    """
    s = None
    for line in file:
        sline = line.strip().split('\t')
       
        # 'M' for metadata (session)
        if sline[1] == 'M' and s is not None:
            yield s
       
        if sline[1] == 'M':
            session_id, record_type, day, user_id = sline
            s = create_session(session_id, day, user_id)
        elif sline[2] == 'Q': # 'Q' for Query
            session_id, time_passed, record_type, serpid, quid, terms = sline[:6]
            url_list = sline[6:]
            s['Queries'].append(create_query(time_passed, serpid, quid, terms, url_list))
        elif sline[2] == 'C': # 'C' for Click
            session_id, time_passed, record_type, serpid, urlid = sline
            s['Queries'][-1]['Clicks'].append(create_click(time_passed, serpid, urlid))
 
def create_session(session_id, day, user_id):
    return { 'SessionID': int(session_id),
              'Day': int(day),
              'USERID': int(user_id),
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
