# install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip install myswl
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
	host='localhost',
	user = 'root', 
	passwd = 'Miggy2011'


	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE bubimsco")

print("All Done!!!!!!")