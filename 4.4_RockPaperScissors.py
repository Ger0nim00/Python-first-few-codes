rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rockpaperscissors = '''

d8888b.  .d88b.   .o88b. db   dD d8888b.  .d8b.  d8888b. d88888b d8888b. .d8888.  .o88b. d888888b .d8888. .d8888.  .d88b.  d8888b. .d8888. 
88  `8D .8P  Y8. d8P  Y8 88 ,8P' 88  `8D d8' `8b 88  `8D 88'     88  `8D 88'  YP d8P  Y8   `88'   88'  YP 88'  YP .8P  Y8. 88  `8D 88'  YP 
88oobY' 88    88 8P      88,8P   88oodD' 88ooo88 88oodD' 88ooooo 88oobY' `8bo.   8P         88    `8bo.   `8bo.   88    88 88oobY' `8bo.   
88`8b   88    88 8b      88`8b   88~~~   88~~~88 88~~~   88~~~~~ 88`8b     `Y8b. 8b         88      `Y8b.   `Y8b. 88    88 88`8b     `Y8b. 
88 `88. `8b  d8' Y8b  d8 88 `88. 88      88   88 88      88.     88 `88. db   8D Y8b  d8   .88.   db   8D db   8D `8b  d8' 88 `88. db   8D 
88   YD  `Y88P'   `Y88P' YP   YD 88      YP   YP 88      Y88888P 88   YD `8888Y'  `Y88P' Y888888P `8888Y' `8888Y'  `Y88P'  88   YD `8888Y' 
                                                                                                                                           
'''

import random

print("by Ger0nim00\n\n")
print(rockpaperscissors)
print("Welcome to Rock Paper Scissors game. \n\nYou wil be playing against the computer. Good Luck! \n\nLoading...\n")

computer_random_list = ["Rock", "Paper", "Scissors"]
random_choice = random.randint(0,2)
game_images = [rock, paper, scissors]

user_choice = int(input("Let's begin amig@, please provide your choise:  type 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors'\n\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number amig@, you lost.")
else:
    print(game_images[user_choice])
    print(f"The computer chose: {random_choice}\n\n")
    print(game_images[random_choice])

    if user_choice == 0 and random_choice == 2:
        print("You Win amig@!!!\n\n")
    elif random_choice ==0 and user_choice  == 2:
        print("You Lost amig@!!\n\n")
    elif random_choice > user_choice:
        print("You lost amig@!!\n\n")
    elif user_choice > random_choice:
        print("You Win amig@!!\n\n")
    elif user_choice == random_choice:
        print("It's a draw amig@!!!\n\n")