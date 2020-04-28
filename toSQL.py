import mysql.connector
from params import host, user, passwd, database
import pandas as pd
import os
import json
import twitchIntegration



twitchAPI = twitchIntegration.twitchAPI()


mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    auth_plugin='mysql_native_password',
    database=database
)



barryPath = os.path.join(os.getcwd(), 'following', 'Barrickinov0001.json')

with open(barryPath) as f:
    data = json.load(f)

userList = []

for i in data['data']:
    userList.append(i['to_id'])

query = twitchAPI.get_users(userList)
response = twitchAPI.get_response(query)


mycursor = mydb.cursor()

for i in response.json()['data']:

    sql = "INSERT INTO persons (user_id, display_name, view_count, broadcaster_type) VALUES (%s, %s, %s, %s)"
    val = (i['id'], i['display_name'], i['view_count'], i['broadcaster_type'])
    mycursor.execute(sql, val)

mydb.commit()

# print(mycursor.rowcount, "record inserted.")

