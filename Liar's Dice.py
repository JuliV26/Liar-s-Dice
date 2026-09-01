import random

class Dice:
    def __init__(self):
        self.dice = []
        self.number_of_dice = 5



    def roll_dice(self):
        self.dice = []

        for i in range(self.number_of_dice):
            self.dice.append(random.randint(1, 6))

    def remove_die(self):
        self.number_of_dice -= 1



    def show_dice(self):
        print("Your dice:", self.dice)

    def count_dice(self, number):
        return self.dice.count(number)


class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice

class Bids:
    def __init__(self):
        self.quantity = 0
        self.number = 0

    def make_bid(self):
        self.quantity = int(input("How many dice? "))
        self.number = int(input("What number? "))

        print(
            "Bid:",
            self.quantity,
            "x",
            self.number
        )

    def check_bid(self, players):
        total = 0

        for player in players:
            total += player.dice.count_dice(self.number)

        if total >= self.quantity:
            return True
        else:
            return False
        
    def liar(self, players):
        result = self.check_bid(players)

        if result:
            print("The bid was TRUE!")
        else:
            print("The bid was FALSE!")
        
class Game:
    def __init__(self):
        self.players = []
        self.bids = Bids()
        self.current_player = 0



    def add_player(self, name):
        dice = Dice()
        player = Player(name, dice)
        self.players.append(player)
    
    def show_players(self):
        for player in self.players:
            print(player.name)


    def start_game(self):
        for player in self.players:
            player.dice.roll_dice()

        print("\nYour dice:")
        self.players[0].dice.show_dice()

        self.bids.make_bid()
        
        while True:
            print("\nWhat do you want to do?")
            print("1. Make higher bid")
            print("2. Call liar")

            choice = input("Choose: ")

            if choice == "1":
                self.bids.make_bid()

            elif choice == "2":
                self.bids.liar(self.players)
                break

            else:
                print("Please choose 1 or 2.")


    

