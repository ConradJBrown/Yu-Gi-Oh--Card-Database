from API import YuGiOhAPI

name = 'Tornado Dragon'
def main():
    card = YuGiOhAPI(name)
    print(card.get_name())
    if card.get_atk():
        print(card.get_atk())
    

main()