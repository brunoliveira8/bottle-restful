import sqlite3 as lite
import sys


def create_tables():
	cur.execute("CREATE TABLE TASKS( ID INTEGER PRIMARY KEY, TITLE CHAR(30))")


def insert_data():
	cur.execute("")
	cur.execute("INSERT INTO TASKS(TITLE) VALUES('task 1')")

con = lite.connect('app.db')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data  

    create_tables()
    insert_data()