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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
     
      ''')
print("Welcome To The Treasure Island.")
print('Your mission is to find the Treasure.')

direction = input("Where do you wanna Go: left or right: ").lower()

if direction == "left":
    wanna_do = input("Do you wanna 'swim' or 'wait' for a boat?").lower()
    if wanna_do == "wait":
        print("You've reached to an island with Three Doors.")
        door_value = input("Choose which Door you wanna use 'Red','Blue' or 'Yellow' .").lower()
        if door_value == "yellow":
            print("YOU WIN!!! You've found the treasure.")
        elif door_value == "red":
            print("You're burned bY fire!!! GAME OVER!!! ")
        elif door_value =="blue":
            print("You're eaten by a Beast !!! GAME OVER!!!")
        else:
            print("GAME OVER!!!!")
    else:
        print("You're attacked by a Trout!!! GAME OVER!!!")
else:
    print("You Fall into a Hole!!! GAME OVER!!!")
    
