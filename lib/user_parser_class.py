from session_parser import Session
import itertools, operator

class IndexLoaders(object):
# A class mostly for static access and storage of the index files.
# WARNING : The user index will consume roughly 3GB of memory if provided as an argument.

	user_index = dict()
	session_index = dict()

	# loads the index file generated for users/start/end positions/sessions associated
	# into the global hash user_index_file
	@staticmethod
	def load_user_index_file(user_index_file):
		if len(IndexLoaders.user_index) == 0:
			print 'Starting to load user index hash...'
			with open(user_index_file,'r') as f:
				for line in f:
					s = line.split('\t')
					IndexLoaders.user_index[s[0]] = list() # uid
					IndexLoaders.user_index[s[0]].append(int(s[1])) # start position
					IndexLoaders.user_index[s[0]].append(int(s[2])) # end position
					IndexLoaders.user_index[s[0]].append([int(x) for x in s[3].rstrip().split(',')]) # sessions
			print 'Completed loading of user index hash!'
		else:
			print 'User index file appears to already have entries loaded.'

	# loads the index file generated for sids/start/end positions
	@staticmethod
	def load_session_index_file(session_index_file):
		print 'Starting to load session index hash...'
		if len(IndexLoaders.session_index) == 0:
			with open(session_index_file,'r',) as f:
				for line in f:
					s = line.split('\t')
					IndexLoaders.session_index[s[0]] = list() # sid
					IndexLoaders.session_index[s[0]].append(int(s[1])) # start
					IndexLoaders.session_index[s[0]].append(int(s[2])) # end
			print 'Completed loading of session index hash!'
		else:
			print 'Session index appears to already have entries!'

# a representation of a User class, see test_user_parser for usage
class User(object):
    __slots__ = ('uid', 'sessions')

	# constructor
	def __init__(self, uid, sessions):
		self.uid = uid
		self.sessions = sessions

    ## <Pseudo-code>
    ## returns the dictionary of query-url pair that are rated 2.
    ##   the form is: {(query_1, url_4): session_1, session_3, session_4, (query_2, url_3): session1}
    ## the sessions are the ones in which each query-url pair has been rated 2.
    #def get_queries_rated_2(self):
    #    # if we already have this in the object, return it.
    #    if not queries_rated_2 == None:
    #        return queries_rated_2
    #    # otherwise, compute it
    #    else:
    #        # find and set queries_rated_2
    ## returns the number of times the user has liked the same query-document pair
    ## in past sessions
    #def num_times_rated_2(self, query, url):
    #    # use get_queries_rated_2 for this
    ### (User class end)

	@staticmethod
	# take a uid, construct a user object and associated session objects
	def from_non_sequential_rows(uid, sessions, training_file):
		# uid is the user id
		# sessions are a list of ints of session numbers
		# get the rows associated with a session and toss it off to the Session parser
		ret_sessions = list()
		for session in sessions:
			t_session = IndexLoaders.session_index[session]
			t_session_start = IndexLoaders.session_index[session][0]
			t_session_end= IndexLoaders.session_index[session][1]

			rows = []

			with open(training_file,'r') as f:
				f.seek(t_session_start,0)
				while(f.tell() < t_session_end):
					rows.append(f.readline().split('\t'))
		
			ret_sessions.append(Session.from_rows(session, rows))
		t = User(uid,ret_sessions)
		print t.uid
		print t.sessions
		return User(uid, ret_sessions)

	@staticmethod
	def parse_user_sessions(rows):
		for sid, row in itertools.groupby(rows, key=lambda row:row[0][0]):
			# sid = the first session that the parser runs across for the user
			# a bunch of sessions are all bundled into the generator rows

			row = list(row) # convert generator to values [[[ ]]]
			sid = int(sid)
			
			# print sid, row , '\n'
			# gives rows where all sessions belong to the same user within this grouping
			
			meta = row[0][0]
			assert meta[1] == "M"
			uid = int(meta[3])

			current_sid = sid
			for entry in row:
				session_rows = list()
				session_objects = list()
				# need to create separate session objects when the session number changes
				for line in entry:
					if int(line[0]) != current_sid:
						# create session info for lines saved thus far
						s = Session.from_rows(current_sid, session_rows)
						session_objects.append(s)
						# update current session tracking
						current_sid = int(line[0])
						session_rows = []
					session_rows.append(line)
				# deal with off by one case at the very end
				s = Session.from_rows(current_sid, session_rows)
				session_objects.append(s)
				current_sid = int(line[0])

			# t= User(uid, session_objects)
			# print t.uid, t.sessions
			return User(uid, session_objects)

	# yields each from each line of the given file if it is only a METADATA line
	# captures lines associated with a user and all their sessions
	@staticmethod
	def generator_of_seqential_lists(file_path):
		f = open(file_path)
		prev_user = 0
		rows = list()
		for line in f:
			row = line.rstrip().split('\t')
			if row[1] == 'M':
				if prev_user != int(row[3]):
					prev_user = int(row[3])
					yield rows
					rows = [] 
			rows.append(row)

	@staticmethod
	def parse_from_file(training_file):
		gl =  User.generator_of_seqential_lists(training_file)
		return User.parse_user_sessions(gl)
		
	# representation of a User class
	def __repr__(self,):
		return "User %s" % (self.uid)
