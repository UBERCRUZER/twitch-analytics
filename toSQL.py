import mysql.connector
from params import host, user, passwd


mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    auth_plugin='mysql_native_password'
)


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

print(mydb)