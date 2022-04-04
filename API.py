from numpy import False_
import requests
import json
import pandas as pd
from os.path import exists
import csv


URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
FILE_INVENTORY = 'YuGiOh_Inventory.csv'
INVENTORY = pd.read_csv('Database.csv')

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
    while (add_to_Inv != 'y') or (add_to_Inv != 'n'):
        print('Input invalid. Please enter [y/n]')
        add_to_Inv = input('Would you like to add this card to inv? [y/n] ')
    if add_to_Inv == 'y':
        pd.concat([INVENOTRY, card], ignore_index=True)
        display(INVENORY)
    else:
        print('Card was not added')

main()

       
       



        
