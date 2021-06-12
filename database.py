import mysql.connector as a

mydb = a.connect(host="localhost", user="root", passwd="",database="python")

if mydb.is_connected():
    print("Connected")
else:
    print("Not Connected")

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE TABLE clients (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()

sql = "INSERT INTO clients (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()