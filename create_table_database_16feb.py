import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
#print(mydb) # here we call connection
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test2.test_table(c1 INT ,c2 VARCHAR(50) ,c3 FLOAT ,c4 INT ,c5 VARCHAR(30) )")
mydb.close()