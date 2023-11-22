#!/usr/bin/python3

"""
execute select query on a given database

"""

import MySQLdb
import sys


user_name = sys.argv[1]
key = sys.argv[2]
user_db = sys.argv[3]

connection = MySQLdb.connect(
    host='localhost',
    user=user_name,
    port=3306,
    passwd=key,
    db=user_db
)

cursor = connection.cursor()

query = 'SELECT * FROM states ORDER BY states.id'

cursor.execute(query)  # query the database
output = cursor.fetchall()

# Print output
for row in output:
    print(row)
