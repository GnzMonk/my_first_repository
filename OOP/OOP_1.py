import random as r

class Coin:

    def __init__(self):
        self.__sideup = "орел"

    def toss(self):
        if r.randint(0, 1) == 0:
            self.__sideup == "орел"
        else:
            self.__sideup = "решка"

    def get_sideup(self):
        return self.__sideup

def main():
    my_coin = Coin()
    print(my_coin.get_sideup())
    my_coin.toss()
    print(my_coin.get_sideup())

if __name__ == "__main__":
    main()