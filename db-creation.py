import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Sanskar@1234")

mycursor=mydb.cursor()
# Create database query or show datatbase query
mycursor.execute("show databases")

for db in mycursor:
    print(db)