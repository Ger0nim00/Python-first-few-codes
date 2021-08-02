print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') 
print("by Jacobo Salas\n")
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.") 

print("So you want to find the treasure amigo???\nAaaarrrggghhh, let's see if you make it alive through the valley of shadows where pirates' souls are dwelling around in eternity....\nMuahahaahahahaa \n")



loser = r''' ________  ________  _____ ______   _______           ________  ___      ___ _______   ________     
|\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\  \    /  /|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \  /  / | \   __/|\ \  \|\  \   
 \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \/  / / \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \    / /   \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__/ /     \ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__|/       \|_______|\|__|\|__|'''

winner = r'''  ___    ___ ________  ___  ___          ___       __   ___  ________      
 |\  \  /  /|\   __  \|\  \|\  \        |\  \     |\  \|\  \|\   ___  \    
 \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \    \ \  \ \  \ \  \\ \  \   
  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \  __\ \  \ \  \ \  \\ \  \  
   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \|\__\_\  \ \  \ \  \\ \  \ 
 __/  / /      \ \_______\ \_______\       \ \____________\ \__\ \__\\ \__\
|\___/ /        \|_______|\|_______|        \|____________|\|__|\|__| \|__|
\|___|/                                                                    '''


game_over = True
tunnel_choise1 = input("Let's begin amigo... there is dark tunnel in the beginning of the forrest covered by old, very old trees...\nAt the end you find a ancient gate with 2 doors build by the Incas.... Please select which on you will choose.....\n\nLeft or Right???  \n\n").lower()
if tunnel_choise1 == "left":
    water_choise2 = input("\nVery good amigoo... Now that you have chosen the right door.... you will need to cross the water.\nThe sun is lowering, you might still make it before it get's dark...\n\nWhat wil you do amigo?\n\nSwim or Wait? \n\n").lower()
    if water_choise2 == "wait":
            door_choise3 = input("]\nUuyyyyy mi amigo you have made it so far... that surprises me, you will need to choose again between doors.. but this time they have a special colour... \nBlue, Yellow, Green, Purple or Red..... which one will it be?? \n\n").lower()
            if door_choise3 == "yellow":
                    game_over = False
                    print("YESSSSS MI AMIGOOOOO, CONGRATULATIONS!!!!!! TEQUILA ON THE HOUSE!!!!")
            elif door_choise3 == "red":
                    print("You will be burned by fireeeee muahahahaa...BURNNNN amigo BURNNNNNN")
            elif door_choise3 == "blue":
                    print("YOU ARE DEAD!! You will be served as lunch for the LIONS MUAHAHAAAAAHA")
            else:
                    print("YOU ARE DEAD AMIGO, you are bitten by venomnous snake...you will die slowly and painfully muauahaha....DIEEEE AMIGOOO ..!!!")
    else:
            print("YOU ARE DEAD! POOR YOU.... You will drown like  an elephant in the ocean amigoo...Muahahaha ")
            game_over = True
else:
    game_over = True
    print("YOU WILL BE EATEN BY THE ANACONDAA Muahauahahaa...You have chosen the wrong door.... Dieeeeeeee Amigo DIE!!! MUAHHAHAHA\n")
    
if game_over:
    print(loser)
else:
    print(winner)