import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.cyxb0drmxfft.us-east-1.rds.amazonaws.com",
  user="admin",
  password="admin123",
  database="Wadb"
)
'''
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''
mycursor = mydb.cursor()

sql = "insert into Wadb.Wastatus (Contact,Status,Creation_date) VALUES ('7287075568','Offline',NOW())"
# val = ("John", "Highway 21")
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record inserted.");