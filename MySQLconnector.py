import mysql.connector
myDb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Abhisw@28',
    db ='iacsd'
)

print(myDb)

mycursor = myDb.cursor()
mycursor.execute('show tables')

for i in mycursor:
    print(i)
    
mycursor.execute("SELECT * FROM my_emp")
my_result = mycursor.fetchall() # we get a tuple
print(my_result)