import sys
import socket
import string
from os.path import isfile
from MAIL import *
from PLUGIN import *

if __name__ == "__main__":

	#general settings
	HOST="irc.freenode.net"
	PORT=6667
	NICK="MauBot"
	IDENT="maubot"
	REALNAME="MauritsBot"
	readbuffer=""
	# password for killing daemon via irc
	PASSWORD="quit"
	#options for commandline
	
	# DEAMON switch
	
	## IRC
	# server, HOST
	# PORT
	# NICK
	# IDENT
	# REALNAME
	# irc channel
	
	## MAIL
	# FROM
	# email HOST
	# email PORT
	# username
	# password
	
	# plug-in to use for logging
	DB = use_plugin("SQLITE")
	
	## DB
	#
	DATABASE = "example.db"
	if not isfile(DATABASE):
		DB.createTable(DATABASE)
	
	#connecting to server and sending appropriate orders 
	#registering the nick and joining a channel
	irc=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	irc.connect((HOST, PORT))
	irc.send("NICK %s\r\n" % NICK)
	irc.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
	irc.send("JOIN #irclib\r\n")

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
			elif ((line[1] == "PRIVMSG") & (line[2] == NICK)):
				DB.addEntry(DATABASE, line[1], line[0].split("!")[0][1:], " ".join(line[3:]))
				print line
				
				#
				# ORDERS
				#
				
				#SEND adress adress ...
				# sends the log to the given adresses
				if (line[3][1:] == "SEND"):
					for address in line[4:]:
						#sendEmail(address, DATABASE)
						irc.send("PRIVMSG %s :Sending log to %s\r\n" % (line[0].split("!")[0][1:], address))
				
				#SEEN person person ...
				# tells when persons where last seen in chatroom
				elif (line[3][1:] == "SEEN"):
					for person in line[4:]:
						seen = DB.lastSeen(DATABASE, person)
						irc.send("PRIVMSG %s :%s was last seen %s\r\n" % (line[0].split("!")[0][1:], person, seen))
			
				elif (line[3][1:] == "QUIT"):
					if len(line) > 4:
						if line[4] == PASSWORD:
							irc.send("PRIVMSG %s :Bye Bye\r\n" % line[0].split("!")[0][1:])
							irc.send("QUIT\r\n")
							exit()