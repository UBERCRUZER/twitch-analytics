import requests, json, sys

secretFile = open("secret.txt")
secret = secretFile.read()
secretFile.close()

BASE_URL = 'https://api.twitch.tv/helix/'
CLIENT_ID = 'z7foqecgb543nv0n7jb7chs51m1lfl'
HEADERS = {'Client-ID': CLIENT_ID}
INDENT = 4

# get response from twitch API call
def get_response(query):
    url  = BASE_URL + query
    response = requests.get(url, headers=HEADERS)
    return response

# used for debugging the result
def print_response(response):
    response_json = response.json()
    print_response = json.dumps(response_json, indent=INDENT)
    print(print_response)

# get the current live stream info, given a username
def get_user_streams_query(user_login):
    return 'streams?user_login={0}'.format(user_login)

def get_user_query(user_login):
    return 'users?login={0}'.format(user_login)

def get_user_videos_query(user_id):
    return 'videos?user_id={0}&first=50'.format(user_id)

def get_followers_to(user_id):
    return 'users/follows?to_id={0}&first=50'.format(user_id)

def get_games_query():
    return 'games/top'