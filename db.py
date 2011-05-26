import sqlite3

def createTable(database):
	con = sqlite3.connect(database, isolation_level=None)
	cur = con.cursor()
	cur.execute("create table irc (id INTEGER PRIMARY KEY, time TEXT, sort TEXT, who TEXT, message TEXT)")
	# datetime('now')
	con.commit()
	cur.close()
	
def addEntry(database, order, who, message):
	con = sqlite3.connect(database)
	cur = con.cursor()
	cur.execute("insert into irc values (NULL, datetime('now', 'localtime'),?,?,?)", (order.decode('utf-8'), who.decode('utf-8'), message.decode('utf-8')))
	con.commit()
	cur.close()
	
def lastSeen(database, person):
	con = sqlite3.connect(database)
	cur = con.cursor()
	#seen = 
	cur.execute("select * from irc where who=? ORDER BY time DESC LIMIT 1" , [person.decode('utf-8')])
	con.commit()
	cur.close()
	
	seen = cur.fetchall()
	if seen:
		return seen[0][1]
	else:
		return "never"