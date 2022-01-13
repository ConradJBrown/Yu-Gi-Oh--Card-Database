from numpy import False_
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
        self.ID = df['id'].item()
        self.NAME = df.name.item()
        self.TYPE = df['type'].item()
        self.DESC = df['desc'].item()
        self.RACE = df.race.item()
        self.ARCHETYPE = df.archetype.item()
        self.IMAGE = df.card_images.item()

        if 'Monster' in self.TYPE:
            self.ATTACK = df['atk'].item()
            self.DEFENCE = df['def'].item()
            self.LEVEL = df.level.item()
            self.ATTRIBUTE = df.attribute.item()
        else:
            self.ATTACK = False
            self.DEFENCE = False
            self.LEVEL = False
            self.ATTRIBUTE = False
       
        
        


    def get_name(self):
        return self.NAME

    def get_atk(self):
        return self.ATTACK

    def get_def(self):
        return self.DEFENCE

    def get_desc(self):
        return self.DESC

    def get_ID(self):
        return self.ID

    def get_type(self):
        return self.TYPE

    def get_race(self):
        return self.RACE

    def get_archetype(self):
        return self.IMAGE
    
    def get_level(self):
        return self.LEVEL

    def get_attribute(self):
        return self.ATTRIBUTE

        
