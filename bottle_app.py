from bottle import route, run, template
import sqlite3 as lite
import json, os

@route('/')
def index():
    return "Welcome to my rest api"

@route('/task/:id', method='GET')
def get_task(id):
	
	if  os.path.isfile('app.db'):
		con = lite.connect('app.db')
		
		with con:
			con.row_factory = lite.Row
			cur = con.cursor() 
			cur.execute('SELECT * from TASKS where ID={}'.format(id))
			row = cur.fetchone()
			return { "id" : row['ID'],  "title": row['TITLE']}

run(host='localhost', port=8080)