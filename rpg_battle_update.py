#RPG Battle game
import random
import time

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 500

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print ("{0} takes fatal damage from {1}, with {2} overkill!"
                       .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes fatal damage from {1}!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                  .format(self.name.capitalize(), damage_amount, attacker))

    def show_name(self):
        return self.name

    def move1(self):
        self.move1_rand = random.randint(15, 30)
        return self.move1_rand

    def move2(self):
        self.move2_rand = random.randint(30, 60)
        return self.move2_rand

    def defence_charge(self):
        self.health += defence_amount
        print("{0} casts a barrier, adding {1} to their health!"
              .format(self.name.capitalize(), defence_amount))

    @classmethod
    def get_user_input(self):
        name = input("Hello there, what is your name? ")
        return self(name)

class Demon:
    def __init__(self, name):
        self.name = name
        self.health = 1500

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} takes fatal damage from {1}, with {2} overkill!"
                        .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes fatal damage from {1}!"
                        .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                    .format(self.name.capitalize(), damage_amount, attacker))

    def move1(self):
        self.move1_rand = random.randint(15, 30)
        return self.move1_rand

    def move2(self):
        self.move2_rand = random.randint(25,40)
        return self.move2_rand

    def move3(self):
        self.ultimate = int(2000)
        return self.ultimate

def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def move_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Re-enter your choice.")

def demon_move_selection(health):
    sleep_time = random.randrange(2, 5)
    print("You dare defy me?!")
    time.sleep(sleep_time)

    if (health <= 1300):
        print("Heh, you have actually managed to leave a scratch, good, "
              "it makes this fight more interesting!")
        return random.randint(1, 2)
    elif (health <= 1500):
        return random.randint(1, 2)


def play_round(demon, hero):
    game_in_progress = True
    current_player = demon

    while game_in_progress:
        if (current_player == demon):
            current_player = hero
        else:
            current_player = demon

        print()
        print(
            "You have {0} health remaining and the "
            "Demon Lord has {1} health remaining."
            .format(hero.health, demon. health))
        print()

        if (current_player == hero):
            print("Available attacks:")
            print("1) Quick Punch")
            print("2) Mega Punch")
            print("3) Absolute Defence")
            move = move_selection()
        else:
            move = demon_move_selection(demon.health)

        if (move == 1):
            damage = Hero(hero)
            demon_damage = Demon(demon)
            if (current_player == hero):
                demon.calculate_damage(damage.move1(), hero.name.capitalize())
            else:
                hero.calculate_damage(demon_damage.move1(), demon.name.capitalize())
        elif (move == 2):
            damage = Hero(hero)
            demon_damage = Demon(demon)
            if (current_player == hero):
                demon.calculate_damage(damage.move2(), hero.name.capitalize())
            else:
                hero.calculate_damage(demon_damage.move2(), demon.name.capitalize())

        if (hero.health == 0):
            print("Sorry, you lose!")
            game_in_progress = False

        if (demon.health == 0):
            print("Congratulations, you beat the Demon Lord!")
            game_in_progress = False


def gameGreeting():
    print("Welcome to the RPG Hero Battle game!")

    demon = Demon("Demon Lord Iruma")

    name = input("Hello there, what is your name? ")
    print("Ahhhh....yes...yes! You are the hero! Hero", name, "!")
    print("You have come at a most fortunate time, you must defeat the Demon Lord!\nHe threatens us all!")
    hero = Hero(name)

    keep_playing = True

    while (keep_playing is True):
        demon.health = 1500
        hero.health = 500
        play_round(demon, hero)
        print()
        response = input("Play another round? (Y/N)")
        if (response.lower() == "n"):
            break

gameGreeting()