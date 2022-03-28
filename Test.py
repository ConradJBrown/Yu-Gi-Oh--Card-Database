from API import YuGiOhAPI


def main():
    name = input("Card name: ")
    card = YuGiOhAPI(name)
    print(card.get_name())
    if card.get_atk():
        print(card.get_atk())
    else:
        print(card.get_type())
    

main()
