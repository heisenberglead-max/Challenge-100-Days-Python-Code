import random
import string

alphabets = list(string.ascii_letters)
# print(alphabets)

special_char = list(string.punctuation)
# print(special_char)
    
numbers = list(range(0,10))
# print(numbers)    

rq_alphabets = int(input("How many letters you want in your password: "))
rq_special_char = int (input("How many special characters you want in your password: "))
rq_numbers = int(input("How many numbers you want in your password: "))
password= []
for alph in range(0,rq_alphabets):
    password.append(random.choice(alphabets))

for spcl in range(0,rq_special_char):
    password.append(random.choice(special_char))
    
for num in range(0,rq_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

new_pw = ""
for char in password:
    new_pw += str(char);
    
print(f"The random password generated for you is :  {new_pw} ")