#Install Mysql on my computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector


dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'ddbs3421',

	)

#prepare a cursuo object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")