#!/usr/bin/python

import mysql.connector
import datetime

day = datetime.datetime.now().day

# Open database connection
db = mysql.connector.connect(host="localhost",database="word_data",user="root" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select count(*) from words")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

hashed_number = day % data[0]-1

query = str("SELECT * FROM words LIMIT ")+ str(hashed_number)+",1"

cursor.execute(query)

# Fetch a single row using fetchone() method.
data_row = cursor.fetchone()

print data_row

# disconnect from server
db.close()

