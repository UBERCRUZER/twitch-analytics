import twitchIntegration
import json


# user_login = 'martinimonsters'

user_id = '42599044'

query = twitchIntegration.get_followers_to(user_id)
response = twitchIntegration.get_response(query)

twitchIntegration.print_response(response)



with open("first50.json", "w") as outfile: 
    json.dump(response.json(), outfile) 
