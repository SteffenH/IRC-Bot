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
#MAIL
	parser.add_argument('--mhost', action='store', dest='mail_host',
						help='eMail host')
	parser.add_argument('--maddress', action='store', dest='mail_address',
						help='eMail address')
	parser.add_argument('--musername', action='store', dest='mail_username',
						help='eMail username')
	parser.add_argument('--mpass', action='store', dest='mail_password',
						help='eMail password')
	parser.add_argument('--msubject', action='store', dest='mail_subject',
						help='eMail subject',
						default="IRC Log")
#PLUGIN
	parser.add_argument('--plugin', action='store', dest='plugin',
						help='logging plugin',
						default="SQLITE")
	parser.add_argument('--plugin-location', action='store', dest='plugin_location',
						help='absolute location of logs')

	return parser.parse_args()