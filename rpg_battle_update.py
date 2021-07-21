#RPG Battle game
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 2000

    def show_name(self):
        return self.name

    def move_1(self):
        self.move1_rand = random.randint(15, 30)
        return self.move1_rand

    def move_2(self):
        self.move2_rand = random.randint(30, 60)
        return self.move2_rand

    def defence_charge(self):
        self.health += 2000

    @classmethod
    def get_user_input(self):
        name = input("Hello there, what is your name? ")
        return self(name)

class Demon:
    def __init__(self, name):
        self.name = name
        self.health = 4000

    def attack1(self):
        self.move1_rand = random.randint(15, 30)
        return self.move1_rand

    def attack2(self):
        self.move2_rand = random.sample(range(15,30), 3)

        return self.move2_rand

    def attack3(self):
        self.ultimate = int(9999)
        return self.ultimate

player = Hero.get_user_input()

def gameGreeting():
    print("Ahhhh....yes...yes! You are the hero! Hero", player.show_name())
    print("You have come at a most fortunate time, you must defeat the Demon Lord!\nHe threatens us all!")

gameGreeting()

