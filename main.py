from flask import Flask, request

from utils import return_request as rr, mean as m, generate_users as gu, count_astronauts as ca

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


#---DB layer init ----
import sqlite3

db = sqlite3.connect('sample.db')
cur = db.cursor()
sql_create_query = '''CREATE TABLE IF NOT EXISTS phones (contactName text, phoneValue text)'''
cur.execute(sql_create_query)
#----

# /phones/create/, /phones/read/, /phones/update/, /phones/delete/)

#Creating a record with two params: 'contactName' and 'phoneValue'
# Sample request: http://127.0.0.1:5000/phones/create/?contactName=Nikolay&phoneValue=5687234723

@app.route('/phones/create/')
def phones_create():
    db = sqlite3.connect('sample.db')
    cur = db.cursor()
    contact_name = request.args['contactName']
    phone_value = request.args['phoneValue']
    with db:
        cur.execute('''INSERT INTO phones (contactName, phoneValue) VALUES (?, ?)''', (contact_name, phone_value))
        db.commit()
        return f'Record Created - {contact_name}, {phone_value}'

#Reading user records by contact name
# Sample request: http://127.0.0.1:5000/phones/read/?contactName=Nikolay

@app.route('/phones/read/')
def phones_read():

    db = sqlite3.connect('sample.db')
    cur = db.cursor()
    contact_name = request.args['contactName']
    with db:
        sql_query = "SELECT * FROM phones WHERE contactName = ?"

        cur.execute(sql_query, (contact_name,))
        return_data = cur.fetchall()
        if not return_data:
            return 'Record not found'
        else:
            return_data=return_data

    return str(return_data)

#Updating the phone number of any given user:
# Sample request: http://127.0.0.1:5000/phones/update/?contactName=Nikolay&phoneValue=1234556789
@app.route('/phones/update/')
def phones_update():

    db = sqlite3.connect('sample.db')
    cur = db.cursor()
    contact_name = request.args['contactName']
    phone_value = request.args['phoneValue']
    with db:
        sql_query = "UPDATE phones set phoneValue = ? WHERE contactName = ?"
        cur.execute(sql_query, (phone_value, contact_name))
        db.commit()
        return str(f'Record Updated {contact_name} {phone_value} ')

#Deleting records of any given user
# Sample request:
@app.route('/phones/delete/')
def phones_delete():

    db = sqlite3.connect('sample.db')
    cur = db.cursor()
    contact_name = request.args['contactName']
    with db:
        sql_query = "DELETE FROM phones WHERE contactName = ?"
        cur.execute(sql_query, (contact_name, ))
        db.commit()
        return f'Record for the name {contact_name} deleted'

@app.route('/')
def hello_world():
    return 'Hello World!'





@app.route('/requirements/')
def requirements():
    result = rr()
    return result

@app.route('/mean/')
def mean():
    result1 = m()
    return result1

@app.route('/generate-users/')
def generate_users():
    n = int(request.args.get('number'))
    if not n:
        n = 10
    result = gu(n)
    return result

@app.route('/space/')
def space():
    result = ca()
    return result








