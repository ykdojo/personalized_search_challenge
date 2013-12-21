from session_parser import Session
import itertools

class IndexLoaders(object):

	user_index = dict()
	session_index = dict()

	# loads the index file generated for users/start/end positions/sessions associated
	# into the global hash user_index_file
	@staticmethod
	def load_user_index_file(user_index_file):
		print 'Starting to load user index hash...'
		with open(user_index_file,'r') as f:
			for line in f:
				s = line.split('\t')
				IndexLoaders.user_index[s[0]] = list() # uid
				IndexLoaders.user_index[s[0]].append(int(s[1])) # start position
				IndexLoaders.user_index[s[0]].append(int(s[2])) # end position
				IndexLoaders.user_index[s[0]].append([int(x) for x in s[3].rstrip().split(',')]) # sessions
		print 'Completed loading of user index hash!'

	# loads the index file generated for sids/start/end positions
	@staticmethod
	def load_session_index_file(session_index_file):
		print 'Starting to load session index hash...'
		with open(session_index_file,'r',) as f:
			for line in f:
				s = line.split('\t')
				IndexLoaders.session_index[s[0]] = list() # sid
				IndexLoaders.session_index[s[0]].append(int(s[1])) # start
				IndexLoaders.session_index[s[0]].append(int(s[2])) # end
		print 'Completed loading of session index hash!'

class User(object):
	# need to load the dictionary of the user_index file and pass as a reference
	# to this function to access the training file
	# the loaded dictionary should be in the following format 
	# user_index_dict{ int : { 'start' : int, 'end' : int, 'sessions', string } }
	# where the first int is the uid
	# and sessions is a string delimited by commas

	def __init__(self, uid, sessions):
		self.uid = uid
		self.sessions = sessions

	@staticmethod
	# take a uid, construct a user object and associated session objects
	def from_rows(uid, sessions, training_file):
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
		#print t
		#print t.sessions
		return User(uid, ret_sessions)
		
	@staticmethod
	def parse(rows,training_file):
		for user, rows in itertools.groupby(rows,key=lambda row:row[3]):
			User.from_rows(user, [x[0] for x in rows],training_file)

	# yields each from each line of the given file
	@staticmethod
	def generator_of_lists(file_path):
		f = open(file_path)
		for line in f:
			row = line.split()
			if row[1] == 'M':
				yield row
	
	# input is file_path -> output is session generator
	@staticmethod
	def parse_from_file(training_file):
		gl = User.generator_of_lists(training_file)
		return User.parse(gl,training_file)

	def __repr__(self,):
		return "User %s" % (self.uid)


