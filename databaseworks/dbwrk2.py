import sqlite3
connection=sqlite3.connect('employee.db')
cursor=connection.cursor()
cursor.execute("CREATE TABLE employe (NAME VARCHAR[50],AGE INT[10],ID INT[10],SALARY INT[25],JOINING DATE INT[20],BOND EXPIRING DATE INT[20])")
cursor.execute("INSERT INTO employe(name,age,id,salary,joining date,bond expiry date)VALUES('Karthika',28,1,20000,15-04-2023,15-05-2025)")
cursor.execute("INSERT INTO employe(name,age,id,salary,joining date,bond expiry date)VALUES('Arun',24,2,13000,20-06-2024,22-06-2026)")
cursor.execute("INSERT INTO employe(name,age,id,salary,joining date,bond expiry date)VALUES('Rithwik',23,3,15000,12-06-2024,15-08-2026)")
cursor.execute("INSERT INTO employe(name,age,id,salary,joining date,bond expiry date)VALUES('Sreya',25,4,14000,24-07-2024,18-08-2026)")
cursor.execute("INSERT INTO employe(name,age,id,salary,joining date,bond expiry date)VALUES('Binu',29,5,23000,10-10-2022,16-08-2024)")
cursor.execute("SELECT*FROM employe")
rows=cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()

