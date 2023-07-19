import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb) # here we call connection
mycursor = mydb.cursor() #with the help of cursor we can read the data one by one
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)