import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Sanskar@1234", database="job_application_system")

mycursor=mydb.cursor()
# Add query of table creation
mycursor.execute("show tables")

# after creating here is the showing command of all  tables
for tb in mycursor:
    print(tb)