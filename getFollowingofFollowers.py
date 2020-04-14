import twitchIntegration
import json
import pandas as pd 
import numpy as np
import os
import time
import random



def apiCoolDown (apiCount):
    if apiCount % 500 == 0:
        time.sleep(60)
        print('60 second pause')
    if apiCount % 50 == 0:
        print(apiCount)

followers = pd.read_csv('followers.csv')

followersList = followers['from_id'].tolist()

sampSize = 100

indexSamp = random.sample(np.arange(len(followersList)).tolist(), sampSize)

session = twitchIntegration.twitchAPI()

followerSamp = [followersList[i] for i in indexSamp]

apiCount = 0
errorCount = 0

for user_id in followerSamp:
    try:
    # user_id = followersList[25487]

        query = session.get_followers_from(user_id, first=100)
        response = session.get_response(query)
        apiCount = apiCount + 1
        apiCoolDown(apiCount)

        totalFollowing = response.json()['total']

        if totalFollowing > 100:
            numLoops = int(((totalFollowing-1) / 100))
            cursor = response.json()['pagination']['cursor']

            userName = response.json()['data'][0]['from_name']
            fileName = '{0}0000.json'.format(userName)
            filePath = os.path.join(os.getcwd(), 'following', fileName)

            with open(filePath, "w") as outfile: 
                json.dump(response.json(), outfile) 

            for loopNum in range(1,numLoops+1):
                query = session.get_followers_from(user_id, first=100, after=cursor)
                response = session.get_response(query)
                apiCount = apiCount + 1
                apiCoolDown(apiCount)

                userName = response.json()['data'][0]['from_name']
                fileName = '{0}{1}.json'.format(userName,str(loopNum).zfill(4))
                filePath = os.path.join(os.getcwd(), 'following', fileName)

                with open(filePath, "w") as outfile: 
                    json.dump(response.json(), outfile) 
                
                cursor = response.json()['pagination']['cursor']

        else: 
            userName = response.json()['data'][0]['from_name']
            fileName = '{0}0000.json'.format(userName)
            filePath = os.path.join(os.getcwd(), 'following', fileName)

            with open(filePath, "w") as outfile: 
                json.dump(response.json(), outfile) 
    except:
        print('Eff.')

        errorCount = errorCount + 1
        print(errorCount)

        # dump file 
        fileName = 'err{0}.json'.format(str(errorCount).zfill(4))
        filePath = os.path.join(os.getcwd(), fileName)

        with open(filePath, "w") as outfile: 
            json.dump(response.json(), outfile) 
        
        