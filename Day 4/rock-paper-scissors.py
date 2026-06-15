import random

symbol = [  'game','''  
___________
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''' ,
 '''  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) '''
,
'''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
]
print("Welcome!! to Rock, Paper & Scissors Game.");
print("Please!! Choose 1 for rock, 2 for paper & 3 for scissors.")
user_input = int(input())
print(f"You've choosen:{symbol[user_input]} ")
computer_input = random.randint(1,3)
print(f"Computer've choosen:{symbol[computer_input]} ")
if user_input == computer_input:
    print("Its a draw.")
elif user_input==1 and computer_input==2:
    print("Computer won!!!")
elif user_input==1 and computer_input==3:
    print("You've won!!!")
elif user_input==2 and computer_input==1:
    print("You've won!!!")
elif user_input==2 and computer_input==3:
    print("Computer won!!!")
elif user_input==3 and computer_input==2:
    print("You've won!!!")
elif user_input==3 and computer_input==1:
    print("Computer won!!!")

