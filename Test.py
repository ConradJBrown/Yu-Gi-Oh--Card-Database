from API import YuGiOhAPI
import pandas as pd

def main():
    name = input("Card name: ")
    card = YuGiOhAPI(name)
    while card.get_pass == False:
        name = input("Card name: ")
        card = YuGiOhAPI(name)

    print(card.get_name())
    if card.get_atk():
        print(card.get_atk())
    else:
        print(card.get_type())
    
def add_Card(card):
  return  

main()
