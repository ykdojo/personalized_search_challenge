## Informally test session_parser.py

import os
import sys
import unittest 
this_file_path = os.path.realpath(__file__) # this file's path
home_dir = os.path.dirname(os.path.dirname(this_file_path))
sys.path.insert(0, home_dir + "/script") # for importing functions

import session_parser as sp
#gl = sp.generator_of_lists(home_dir + '/data/train_head')
gl = sp.generator_of_lists(home_dir + '/data/train_small')
#f = open(home_dir + '/data/train', 'rb')
session_generator = sp.parse(gl)
sessions = [session_generator.next() for i in range(10)]


"""
Throughly Testing Sessions 3

2 Queries
1 Click Event

"""

#Class for Testing Sessions 3
class test_sessions_3(unittest.TestCase):
    """
    Testing Session MetaData

        Session metadata (TypeOfRecord = M):

        SessionID TypeOfRecord Day USERID

    """
    
    def testing_sessions_3_sid(self):
        self.assertEqual(sessions[3].sid, 3)

    def testing_sessions_3_day(self):
        self.assertEqual(sessions[3].day, 13)

    def testing_sessions_3_user(self):
        self.assertEqual(sessions[3].user, 1)

    """
    Testing Sessions Queries

        Query action (TypeOfRecord = Q or T):

        SessionID TimePassed TypeOfRecord SERPID QueryID ListOfTerms ListOfURLsAndDomains

    """

    def testing_sessions_3_queries_0_time(self):
        self.assertEqual(sessions[3].queries[0].time, 0)

    def testing_sessions_3_queries_0_serp(self):
        self.assertEqual(sessions[3].queries[0].serp, 0) 
        
    def testing_sessions_3_queries_0_query(self):
        self.assertEqual(sessions[3].queries[0].query, 5239394) 

    def testing_sessions_3_queries_0_terms(self):
        self.assertEqual(sessions[3].queries[0].terms, [2365113,2856206,2491775])

    def testing_sessions_3_queries_0_hits(self):
        self.assertEqual(sessions[3].queries[0].hits, [(16457319, 1712204), (35513272, 3344594), (50566741, 4217515), (8699936, 1032002), (19587096, 2024884), (52534052, 4295962), (16398219, 1711944), (14941390, 1549526), (45726575, 3933621), (3870230, 510830)])

    def testing_sessions_3_queries_0_clicks(self):
        self.assertEqual(sessions[3].queries[0].clicks, [])

    def testing_sessions_3_queries_1_time(self):
        self.assertEqual(sessions[3].queries[1].time, 76)

    def testing_sessions_3_queries_1_serp(self):
        self.assertEqual(sessions[3].queries[1].serp, 1) 
        
    def testing_sessions_3_queries_1_query(self):
        self.assertEqual(sessions[3].queries[1].query, 5239405) 

    def testing_sessions_3_queries_1_terms(self):
        self.assertEqual(sessions[3].queries[1].terms, [2365113,2856206,2491775,4219157,2383044])

    def testing_sessions_3_queries_1_hits(self):
        self.assertEqual(sessions[3].queries[1].hits, [(16457319, 1712204), (35513272, 3344594), (19587095, 2024884), (54638321, 4409573), (70294280, 5173294), (29007584, 2844548), (65574293, 4975723), (60082408, 4671429), (36666362, 3411741), (33566096, 3248439)])

    """
    Testing Click Event

        Click action (TypeOfRecord = C):

        SessionID TimePassed TypeOfRecord SERPID URLID

    """
    
    def testing_sessions_3_queries_1_clicks_0_time(self):
        self.assertEqual(sessions[3].queries[1].clicks[0].time, 162)
        
    def testing_sessions_3_queries_1_clicks_0_serp(self):
        self.assertEqual(sessions[3].queries[1].clicks[0].serp, 1)
        
    def testing_sessions_3_queries_1_clicks_0_url(self):
        self.assertEqual(sessions[3].queries[1].clicks[0].url, 35513272)

    def testing_sessions_3_queries_1_clicks_0_satifisfaction(self):
        self.assertEqual(sessions[3].queries[1].clicks[0].satisfaction(), 2)
        


#Unit Test Begins Here
if __name__ == '__main__':
    unittest.main()


