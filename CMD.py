import argparse
# http://www.doughellmann.com/PyMOTW/argparse/

def cmd():
	parser = argparse.ArgumentParser()
#IRC
	parser.add_argument('-s', action='store', dest='host',
						help='IRC server')
	parser.add_argument('-p', action='store', dest='port',
						help='IRC port')
	parser.add_argument('-n', action='store', dest='nick',
						help='IRC nick')
	parser.add_argument('-i', action='store', dest='ident',
						help='IRC ident')
	parser.add_argument('-r', action='store', dest='real_name',
						help='IRC real name')
#DAEMON
	parser.add_argument('-D', action='store_false', default=True,
						dest='deamon',
						help='Deactivate deamon behaviour')
	parser.add_argument('-d', action='store', dest='deamon_stop',
						help='Stopping (-d stop) or restarting (-d restart) daemon')
						
	
	return parser.parse_args()