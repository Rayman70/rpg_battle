#RPG Battle game
import random

print("Hello there, what is your name? ")
player = str(input()) #This will be the player name input
print("Ahhhh....yes...yes! You are the hero! Hero", player)
print("You have come at a most fortunate time, you must defeat the Demon Lord!\nHe threatens us all!")

hero = int(2000)    #Health values
demon_lord = int(4000)

counter = 0

while True:
    move1_rand = random.randint(15, 30)
    move2_rand = random.randint(50, 80)
    counter += 1
    choice = input("Use one of your moves! 1/2: ")

    if choice == "1":
        move1 = ("Slash attack! You have done", move1_rand, "damage!")
        demon_lord = int(demon_lord - move1_rand)
        print(move1)
        print("Demon Lord: ", demon_lord)
        print("Turn", counter)
        break

    elif choice == "2":
        move2 = ("Grand Punisher!", "You have done", move2_rand, "damage!")
        demon_lord = int(demon_lord - move2_rand)
        print(move2)
        print("Demon Lord: ", demon_lord)
        print("Turn", counter)
        break

    else:
        print("Try again")

print("Now it is the Demon Lord's turn!")

dl_move1 = int(40)
attack1 = ("Petty insect, take my 'Fire' attack! You have taken", dl_move1, "damage!")
hero = int(hero - dl_move1)
print(attack1)
print("Hero: ", hero)

while True:
    move1_rand = random.randint(15, 30)
    move2_rand = random.randint(50, 80)
    counter += 1
    choice = input("Use one of your moves! 1/2: ")

    if choice == "1":
        move1 = ("Slash attack! You have done", move1_rand, "damage!")
        demon_lord = int(demon_lord - move1_rand)
        print(move1)
        print("Demon Lord: ", demon_lord)
        print("Turn", counter)
        break

    elif choice == "2":
        move2 = ("Grand Punisher!", "You have done", move2_rand, "damage!")
        demon_lord = int(demon_lord - move2_rand)
        print(move2)
        print("Demon Lord: ", demon_lord)
        print("Turn", counter)
        break

    else:
        print("Try again")

