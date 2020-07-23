"""
Rock, Paper, Scissors, Lizard, Spock.

Scissors cut paper,
paper covers rock,
rock crushes lizard,
lizard poisons Spock,
Spock smashes scissors,
scissors decapitates lizard,
lizard eats paper,
paper disproves Spock,
Spock vaporizes rock,
and —as it always has— rock crushes scissors.

"""
import random

print("\nRock, Paper, Scissors, Lizard, Spock.\n\nScissors cut paper,\npaper covers rock,\nrock crushes lizard,\nlizard poisons Spock,\nSpock smashes scissors,\nscissors decapitates lizard,\nlizard eats paper,\npaper disproves Spock,\nSpock vaporizes rock,\nand —as it always has— rock crushes scissors.\n\nRock = 1 | Paper = 2 | Scissors = 3 | Lizard = 4 | Spock = 5\n")

win = "It seems that you've won this time.\n"
lose = "Oh... I win\n"
even = "We're even\n"

""" def print_win():
    print(win)
def print_lose():
    print(lose)
def print_even():
    print(even) """

user = int(input("Choose wisely... "))
def sheldon_play():
    global sheldon 
    sheldon = int(random.randrange(1, 5))

sheldon_play()
results = 0
def play(user, sheldon):

    if user == 1 and sheldon == 1:
        print(even)
    elif user == 1 and sheldon == 2:
        print(lose)
    elif user == 1 and sheldon == 3:
        print(win)
    elif user == 1 and sheldon == 4:
        print(win)
    elif user == 1 and sheldon == 5:
        print(lose)
#paper        
    elif user == 2 and sheldon == 1:
        print(win)
    elif user == 2 and sheldon == 2:
        print(even)
    elif user == 2 and sheldon == 3:
        print(lose)
    elif user == 2 and sheldon == 4:
        print(lose)
    elif user == 2 and sheldon == 5:
        print(win)
#scissors
    elif user == 3 and sheldon == 1:
        print(lose)
    elif user == 3 and sheldon == 2:
        print(win)
    elif user == 3 and sheldon == 3:
        print(even)
    elif user == 3 and sheldon == 4:
        print(win)
    elif user == 3 and sheldon == 5:
        print(lose)
#Lizard
    elif user == 4 and sheldon == 1:
        print(lose)
    elif user == 4 and sheldon == 2:
        print(win)
    elif user == 4 and sheldon == 3:
        print(lose)
    elif user == 4 and sheldon == 4:
        print(even)
    elif user == 4 and sheldon == 5:
        print(win)
#Spock
    elif user == 5 and sheldon == 1:
        print(win)
    elif user == 5 and sheldon == 2:
        print(lose)
    elif user == 5 and sheldon == 3:
        print(win)
    elif user == 5 and sheldon == 4:
        print(lose)
    elif user == 5 and sheldon == 5:
        print(even)

user1, user2, user3, user4, user5 = "Rock", "Paper", "Scissors", "Lizard", "Spock"
sheldon1, sheldon2, sheldon3, sheldon4, sheldon5 = "Rock", "Paper", "Scissors", "Lizard", "Spock"

def UX(user, sheldon):
    print("\nYou choosed: ")
    if user == 1:
        print(user1)
    elif user == 2:
        print(user2)
    elif user == 3:
        print(user3)
    elif user == 4:
        print(user4)
    elif user == 5:
        print(user5)
    print("and I ")
    if sheldon == 1:
        print(sheldon1)
    elif sheldon == 2:
        print(sheldon2)
    elif sheldon == 3:
        print(sheldon3)
    elif sheldon == 4:
        print(sheldon4)
    elif sheldon == 5:
        print(sheldon5)
    print("\n")
UX(user, sheldon)
play(user, sheldon)