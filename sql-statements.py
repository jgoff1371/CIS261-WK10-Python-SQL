# Justin Goff
# CIS 261 Week 10: Python SQL Statements
# 12/10/22

import mysql.connector
from mysql.connector import errorcode


'''
Write the Python code for creating a table based on the following SQL statement:
CREATE TABLE phone (
  phone_id INT,
  country_code INT NOT NULL,
  phone_number INT NOT NULL,
  phone_type VARCHAR(12),
  PRIMARY KEY(phone_id)
);

Write the Python code to select rows from the table based on the following SQL statement:
SELECT phone_number
FROM phone
WHERE country_code = ‘US’


Write the Python code to update rows in the table based on the following SQL statement:
UPDATE phone
SET phone_type = ‘MOBILE
WHERE phone_type = ‘CELLULAR’


Write the Python code to delete rows in the table based on the following SQL statement:
DELETE FROM phone
WHERE country_code = ‘XX’


Write the Python code to drop the table based on the following SQL statement:
DROP TABLE phone
'''

acmeConnection = mysql.connector.connect(
    user="acmeuser",
    password="supersecretpassword1",
    host="127.0.0.1",
    database="ACME")

acmeCursor = acmeConnection.cursor()

phoneCreate = ('CREATE TABLE phone ('
               'phone_id INT,'
               'country_code INT NOT NULL,'
               'phone_number INT NOT NULL,'
               'phone_type VARCHAR(12),'
               'PRIMARY KEY(phone_id)')

acmeCursor.execute(phoneCreate)

phoneQuery = ('SELECT phone_number FROM phone'
              'WHERE country_code ="US"')

acmeCursor.execute(phoneQuery)

phoneUpdate = ('UPDATE phone '
               'SET phone_type = MOBILE'
               'WHERE phone_type = CELLULAR')

acmeCursor.execute(phoneUpdate)

phoneDelete = ('DELETE FROM phone'
               'WHERE country_code = XX')

acmeCursor.execute(phoneDelete)

phoneDrop = ('DROP TABLE phone')

acmeCursor.execute(phoneDrop)

acmeCursor.close()

acmeConnection.close()
