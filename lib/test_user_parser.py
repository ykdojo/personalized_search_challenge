from user_parser_class import User
from user_parser_class import IndexLoaders
import session_parser

#IndexLoaders.load_user_index_file('/home/michael/workspace/ML/personalized_search_challenge/data/user_index_small.txt')
#IndexLoaders.load_session_index_file('/home/michael/workspace/ML/personalized_search_challenge/data/session_index_small.txt')

gen =  User.parse_from_file('/home/michael/workspace/ML/personalized_search_challenge/data/small.train')

for i in gen:
	print i

