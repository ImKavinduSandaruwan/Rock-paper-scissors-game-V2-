#Coded by Kavindu Sandaruwan
my_list = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    ]

# 0 = rock, 1 = paper, 2 = scissor
def pics(computer,player):
    print("Computer choose:")
    for i in range(0,3):
        if i == computer:
            print(my_list[i])

    print("You choose :")    
    for i in range(0,3):
        if i == player:
            print(my_list[i])
   
import random
computer = random.randint(0,2)
print(computer)
player = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissor.\n"))
print()

if player < 0 or player > 2:
    print("Enter valid input")

elif computer == 0 and player == 2:
    pics(computer,player)
    print("you lose")

elif computer == 2 and player == 0:
    pics(computer,player)
    print("you win")
    
elif player == computer:
    pics(computer,player)
    print("Its Tie")
    
elif player > computer:
    pics(computer,player)
    print("You win")
    
else:
    pics(computer,player)
    print("You lose")
