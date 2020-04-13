import twitchIntegration
import json
import pandas as pd 
import numpy as np

# user_login = 'martinimonsters'

user_id = '42599044'

query = twitchIntegration.get_followers_to(user_id)
response = twitchIntegration.get_response(query)

twitchIntegration.print_response(response)

with open('first50.json', "w") as outfile: 
    json.dump(response.json(), outfile) 



file2 = 'first50.json'
with open(file2) as train_file:
    dict_train = json.load(train_file)

# converting json dataset from dictionary to dataframe
page1 = pd.DataFrame.from_dict(dict_train['data'])


pd.DataFrame.from_dict(response.json()['data'])
