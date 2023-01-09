#Coded by Kavindu Sandaruwan
import random
play_again = ""
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = ""
    while player not in choices:
        player = input("rock,paper or scissors? : ").lower()

    if player == computer:
        print("coumputer: ",computer)
        print("player: ",player)
        print("Ofs Tie!")

    elif player == "rock":
        if computer == "paper":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you lose!")
        elif computer == "scissors":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you win!")

    elif player == "paper":
        if computer == "rock":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you win!")
        elif computer == "scissors":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you lose!")

    elif player == "scissors":
        if computer == "paper":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you win!")
        elif computer == "rock":
            print("coumputer: ", computer)
            print("player: ", player)
            print("you lose!")

    play_again = input("You want play again? (yes/no): ").lower()
    if play_again != "yes":
        print()
        break
print("Bye")
