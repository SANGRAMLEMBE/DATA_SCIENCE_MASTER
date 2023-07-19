import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
#print(mydb) # here we call connection
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")
mycursor.execute("insert into test2.test_table values(123,'sangramm',234.58,456,'guddu')")

mydb.commit()
mydb.close()