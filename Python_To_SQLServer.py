import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JQ15HRV\SQLEXPRESS;'
                      'Database=TestDB_Python;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TestDB_Python.dbo.Person')

for row in cursor:
    print(row)