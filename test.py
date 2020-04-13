import twitchIntegration
import json
import pandas as pd 
import numpy as np
import os
import time


# user_login = 'martinimonsters'

user_id = '42599044'


sampFile = 'first100.json'
with open(sampFile) as sample:
    sampleReq = json.load(sample)


totalFollowers = sampleReq['total']
totalReq = int(round(totalFollowers / 100))
# totalReq = int(round(500 / 100))

pageinationCursor = None

for reqNum in range(0, totalReq):
    try:
        # loop request
        query = twitchIntegration.get_followers_to(user_id, first=100, after=pageinationCursor)
        response = twitchIntegration.get_response(query)
        
        # 1 second pause keep API limit happy
        time.sleep(2)

        # set pagination cursor for next loop
        pageinationCursor = response.json()['pagination']['cursor']

        # dump file 
        fileNum = str(reqNum).zfill(5)
        fileName = '{0}.json'.format(fileNum)
        filePath = os.path.join(os.getcwd(), 'followers', fileName)

        with open(filePath, "w") as outfile: 
            json.dump(response.json(), outfile) 


        print('Finished', reqNum, 'out of', totalReq)
    except:
        print('Eff.')

        # dump file 
        fileName = 'busted.json'
        filePath = os.path.join(os.getcwd(), 'followers', fileName)

        with open(filePath, "w") as outfile: 
            json.dump(response.json(), outfile) 
        
        break


