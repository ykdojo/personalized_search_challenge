# This was also originally written by another Kaggler.
# https://gist.github.com/poulejapon/7909562

import itertools
from collections import OrderedDict

class Session(object):
 
    __slots__ = ('sid', 'day', 'day', 'user', 'queries')
 
    def __init__(self, sid, day, user, queries):
        self.sid = sid
        self.day = day
        self.user = user
        self.queries = queries
 
    @staticmethod
    def from_rows(session, rows):
        meta = rows[0][1:]
        assert meta[0] == "M"
        day = int(meta[1])
        user = int(meta[2])
        queries = OrderedDict()
        prev_click_action = None # just here to set up the dwell time
        for action_row in rows[1:]:
            action_row = action_row[1:]
            if prev_click_action is not None:
                prev_click_action.dwell_time = int(action_row[0]) - prev_click_action.time
            if action_row[1] in {"Q","T"}:
                prev_click_action = None
                query = QueryEvent.parse(action_row)
                queries[query.serp] = query
            else:
                assert action_row[1] == "C"
                click = ClickEvent.parse(action_row)
                queries[click.serp].clicks.append(click)
                prev_click_action = click
        return Session(session, day, user, queries.values())
 
    def __repr__(self,):
        return "Session<%i,user=%i>" % (self.sid, self.user)
    
class ClickEvent:
 
    __slots__ = ('time', 'serp', 'url', 'dwell_time', )
    
    def __init__(self, time, serp, url):
        self.time = time
        self.serp = serp
        self.url = url
        self.dwell_time = 1000
 
    def print_debug(self, indent):
        print " "*indent, "click", "time=", self.time, "url=", self.url, "dwell_time=", self.dwell_time
 
    def satisfaction(self,):
        if 50 <= self.dwell_time < 400:
            return 1
        elif 400 <= self.dwell_time:
            return 2
        return 0
 
    @staticmethod
    def parse(fields):
        return ClickEvent(
            int(fields[0]),
            int(fields[2]),
            int(fields[3])
        )
 
class QueryEvent(object):
 
    __slots__ = ('time', 'is_test', 'serp', 'query', 'terms', 'hits', 'clicks')
 
    def __init__(self,
        time,
        is_test,
        serp,
        query,
        terms,
        hits):
        self.time = time
        self.is_test = is_test
        self.serp = serp
        self.query = query
        self.terms = terms
        self.hits = hits
        self.clicks = []
        assert len(self.hits)==10
 
    def get_url_domain(self, qurl):
        for (url, domain) in self.hits:
            if url == qurl:
                return domain
        return None
    
    def print_debug(self, indent):
        print " "*indent, "- Query", "time=", self.time, "terms", ",".join(map(str, self.terms)), self.is_test
        print " "*indent, "  Hits", ",".join(map(str, self.hits))
        for click in self.clicks:
            click.print_debug(indent+2)
 
    def urls(self,):
        return zip(*self.hits)[0]
 
    @staticmethod
    def parse(fields): 
        return QueryEvent(
            int(fields[0]),
            (fields[1] == "T"),
            int(fields[2]),
            int(fields[3]),
            map(int, fields[4].split(",")),
            [ 
                tuple(map(int, urldomain.split(",")))
                for urldomain in fields[5:]
                if "," in urldomain
            ]
        )
 
 
    def url_pertinence(self,):
        # returns a dictionary url -> pertinence for the user
        # as described in :
        #   http://www.kaggle.com/c/yandex-personalized-web-search-challenge/details/evaluation
        rates = defaultdict(int)
        for click in self.clicks:
            rates[click.url] = max(click.satisfaction(), rates[click.url])
        return rates


def parse(rows):
    for session, rows in itertools.groupby(rows,key=lambda row:row[0]):
        yield Session.from_rows(int(session), list(rows))

def generator_of_lists(file_path):
    f = open(file_path)
    for line in f:
        row = line.split()
        yield row
