import sqlite3
connection=sqlite3.connect('example.db')
cursor=connection.cursor()
cursor.execute("insert TABLE users (NAME VARCHAR[50],AGE[10],JOB VARCHAR(45),QUALIFICATION VARCHAR[50],GRDAE VARCHAR[10])")
cursor.execute("INSERT INTO users(name,age,job,qualification,grade)VALUES('sreeja',35,'teacher','degree',B)")


