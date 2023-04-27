import mysql.connector
# add a database name
mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Sanskar@1234", database="job_application_system")

mycursor=mydb.cursor()

# write a sql insert querry
sqlform = "insert into jobs(company,job_title,city,work_mode,required_cgpa) values(%s,%s,%s,%s,%s);"

# its a tuple just fill in some values
employees =[('Deloitte','Backend Developer','Bangalore','Offline',8.5),('TCS','Data Scientist','Mumbai','Offline',8.5),('Google','Machine Learning Engineer','Mumbai','Hybrid',9.0),('Amazon','Full Stack Developer','Delhi','Offline',8.5),('Infosys','Systems Engineer','Mumbai','Offline',8.0)]

mycursor.executemany(sqlform,employees)

mydb.commit()