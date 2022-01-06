import requests
import json
import pandas as pd


class YuGiOhAPI:
    #Grabbing the card asked for from the API
    
    def __init__(self, card):
        parameters = {'name': card}
        response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php', params=parameters)
        data = response.json()
        df = pd.DataFrame.from_dict(data['data'])
        self.name = df['name']
        self.desc = df['desc']
        self.atk = df['atk']
        self.defence = df['def']
        self.ID = df['id']
        self.type = df['type']

    def get_name():
        return self.name
    def get_atk():
        return self.atk
    def get_def():
        return self.defence
    def get_desc():
        return self.desc

        
