from numpy import False_
import requests
import json
import pandas as pd
from os.path import exists
import csv


URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
FILE_INVENTORY = 'YuGiOh_Inventory.csv'
PATH_TO_FILE = 'Inventory.csv'
FILE_EXISTS = exists(PATH_TO_FILE)

def CardInfo(card):
    parameters = {'name': card}
    response = requests.get(URL, params=parameters)
    data = response.json()   
    df = pd.DataFrame.from_dict(data['data'])
    pd.set_option('display.max_colwidth', None)
    return df

def main():
    name = input("Card name: ")
    try:
        card = CardInfo(name)
    except:
        print('This card does not exist')
        return
    print(card.desc.to_string(index=False))

    add_to_Inv = input('Would you like to add this card to inv? [y/n] ')
    while (add_to_Inv != 'y') and (add_to_Inv != 'n'):
        print('Input invalid. Please enter [y/n]')
        add_to_Inv = input('Would you like to add this card to inv? [y/n] ')
    if add_to_Inv == 'y':
        Add_Card(card)
    else:
        print('Card was not added')

def Add_Card(card):
    if FILE_EXISTS:
       INVENTORY = pd.read_csv(PATH_TO_FILE)
       card['Stock'] = 1
       INVENTORY = pd.concat([INVENTORY, card])
    else:
        INVENTORY = card
        INVENTORY['Stock'] = 1
    
    INVENTORY.to_csv(PATH_TO_FILE,index=False, header=True)
    print(INVENTORY['name'])
    return

main()

       
       



        
