import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")

print(mydb)

if(mydb):
    print("Connection Successfull")

else:
    print("Connection failed")