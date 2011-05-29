import argparse
# http://www.doughellmann.com/PyMOTW/argparse/

def cmd():
	parser = argparse.ArgumentParser()
#IRC
	parser.add_argument('-s', action='store', dest='host',
						help='IRC server',
						default="irc.freenode.net")
	parser.add_argument('-p', action='store', dest='port', type=int,
						help='IRC port',
						default=6667)
	parser.add_argument('-n', action='store', dest='nick',
						help='IRC nick',
						default="MauBot")
	parser.add_argument('-i', action='store', dest='ident',
						help='IRC ident',
						default="maubot")
	parser.add_argument('-r', action='store', dest='real_name',
						help='IRC real name',
						default="IRC Bot")
	parser.add_argument('-c', action='store', dest='channel',
						help='IRC channel',
						default="irclib")
	parser.add_argument('--pass', action='store', dest='password',
						help='IRC password for closing the bot')
#DAEMON
	parser.add_argument('-D', action='store_false', default=True,
						dest='deamon',
						help='Deactivate deamon behaviour')
	parser.add_argument('-d', action='store', dest='deamon_stop',
						help='Stopping (-d stop) or restarting (-d restart) daemon')
						
	
	return parser.parse_args()