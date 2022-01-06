import requests
import json


parameters = {'name': 'Fluffal Bear'}
response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params=parameters).json()


for obj in response:
    name = obj['data']['name']
    print(name)
#def jprint(obj):
    # create a formatted string of the Python Json object
 #   text = json.dumps(obj, sort_keys=True, indent=4)
  #  print(text)

#jprint(response.json())