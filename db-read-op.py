import mysql.connector
# Add a database name
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="")

mycursor=mydb.cursor()

# do select from query just like in normal sql
# or select the whole tuple
mycursor.execute("")

# it will fecth single value
myresult = mycursor.fetchone()

for row in myresult:
    print(row)

myresult1 = mycursor.fetchall()

for row in myresult1:
    print(row)