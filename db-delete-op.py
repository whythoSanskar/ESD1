import mysql.connector
# Add a database name
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="")

mycursor=mydb.cursor()
# sql delete query
sql = ""

mycursor.execute(sql)

mydb.commit()