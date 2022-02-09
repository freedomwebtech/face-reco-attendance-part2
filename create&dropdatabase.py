import mysql.connector

mydb = mysql.connector.connect(
       host= "192.168.0.102",
       user="freedomtech123",
       password="freedomtech123"
#       database="Attendanceyt"

)
a = mydb.cursor()
#a.execute("CREATE DATABASE Attendanceyt")
#a.execute("CREATE TABLE UserAttendance (Date VARCHAR(30),USERNAME VARCHAR(255),DateTime VARCHAR(255), PRIMARY KEY (Date,USERNAME))")
sql = "DROP DATABASE Attendanceyt"
a.execute(sql)
mydb.commit()
mydb.close()
