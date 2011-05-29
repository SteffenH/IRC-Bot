import sys, time
import socket
import string
from os.path import isfile
from MAIL import *
from PLUGIN import *
from DAEMON import Daemon
from CMD import cmd

def irc(cmd):
	#general settings
		
	# plug-in to use for logging
	dirname = os.path.dirname(cmd.path)
	plugin_path = os.path.join(dirname, "plugins")
	
	DB = use_plugin(cmd.plugin, plugin_path)
	
	DATABASE = os.path.join(plugin_path, "example.db")
	if cmd.plugin_location:
		DATABASE = cmd.plugin_location
	
	if not isfile(DATABASE):
		DB.createTable(DATABASE)
	
	#connecting to server and sending appropriate orders 
	#registering the nick and joining a channel
	irc=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	irc.connect((cmd.host, cmd.port))
	irc.send("NICK %s\r\n" % cmd.nick)
	irc.send("USER %s %s bla :%s\r\n" % (cmd.ident, cmd.host, cmd.real_name))
	irc.send("JOIN #%s\r\n" % cmd.channel)
	
	readbuffer=""
	
	while 1:
		readbuffer=readbuffer + irc.recv(1024)
		temp=string.split(readbuffer, "\n")
		readbuffer=temp.pop()
		
		for line in temp:
			line=string.rstrip(line)
			line=string.split(line)
			
			#keep-alive messages
			if(line[0]=="PING"):
				irc.send("PONG %s\r\n" % line[1])
			
			# username-format: 
			# :NICK!~IDENT@NETWORK
			
			elif ((line[1] == "PART") | (line[1] == "JOIN")):
				DB.addEntry(DATABASE, line[1], line[0].split("!")[0][1:], line[2])
				print line

			#received private message
			elif ((line[1] == "PRIVMSG") & (line[2] == cmd.nick)):
				DB.addEntry(DATABASE, line[1], line[0].split("!")[0][1:], " ".join(line[3:]))
				print line
				
				#
				# ORDERS
				#
				
				#SEND adress adress ...
				# sends the log to the given adresses
				if (line[3][1:] == "SEND"):
					if (cmd.mail_host & cmd.address):
						for address in line[4:]:
							sendEmail(address, DATABASE, cmd)
							irc.send("PRIVMSG %s :Sending log to %s\r\n" % (line[0].split("!")[0][1:], address))
				
				#SEEN person person ...
				# tells when persons where last seen in chatroom
				elif (line[3][1:] == "SEEN"):
					for person in line[4:]:
						seen = DB.lastSeen(DATABASE, person)
						irc.send("PRIVMSG %s :%s was last seen %s\r\n" % (line[0].split("!")[0][1:], person, seen))
			
				elif (line[3][1:] == "QUIT"):
					if len(line) > 4:
						if (cmd.password):
							if line[4] == cmd.password:
								irc.send("PRIVMSG %s :Bye Bye\r\n" % line[0].split("!")[0][1:])
								irc.send("QUIT\r\n")
								exit()

class MyDaemon(Daemon):
	def run(self, cmd):
		irc(cmd)
						
if __name__ == "__main__":
	commands = cmd()
	commands.path = os.path.abspath(sys.argv[0])
	
	if (commands.deamon):
		daemon = MyDaemon('/tmp/daemon-example.pid')
		if not commands.deamon_stop:
			daemon.start(commands)
		elif 'stop' == commands.deamon_stop:
			daemon.stop()
		elif 'restart' == commands.deamon_stop:
			daemon.restart(commands)
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		irc(commands)