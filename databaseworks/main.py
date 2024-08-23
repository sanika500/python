import sqlite3
connection=sqlite3.connect('example.db')
cursor=connection.cursor()
cursor.execute("CREATE TABLE employees1 (NAME VARCHAR[50],AGE[10],JOB VARCHAR(45),QUALIFICATION VARCHAR[50],GRADE VARCHAR[10])")
cursor.execute("INSERT INTO employees1(name,age,job,qualification,grade)VALUES('sreeja',35,'teacher','degree','B')")
cursor.execute("INSERT INTO employees1(name,age,job,qualification,grade)VALUES('anu',28,'engineer','btech','A')")
cursor.execute("INSERT INTO employees1(name,age,job,qualification,grade)VALUES('kavya',20,'student','bsc','B')")
cursor.execute("INSERT INTO employees1(name,age,job,qualification,grade)VALUES('surya',30,'doctor','mbbs','A')")
cursor.execute("SELECT *From employees1")
rows=cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()


