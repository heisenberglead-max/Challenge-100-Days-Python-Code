import random
word_list = [
    "table", "chair", "window", "door", "computer", "phone", "book", "pen", "pencil", "paper",
    "bottle", "cup", "plate", "spoon", "fork", "knife", "clock", "watch", "wallet", "bag",
    "shoe", "sock", "shirt", "pants", "jacket", "hat", "key", "lock", "mirror", "comb",
    "brush", "soap", "towel", "bed", "pillow", "blanket", "lamp", "desk", "shelf", "couch",
    "television", "remote", "camera", "radio", "guitar", "piano", "drum", "ball", "bat", "bicycle",
    "car", "truck", "bus", "train", "airplane", "boat", "ship", "wheel", "engine", "tire",
    "hammer", "screwdriver", "wrench", "pliers", "saw", "nail", "screw", "drill", "ladder", "rope",
    "basket", "box", "bucket", "shovel", "broom", "mop", "sponge", "scissors", "tape", "glue",
    "candle", "match", "lighter", "pipe", "wire", "cable", "plug", "switch", "battery", "bulb",
    "coin", "bill", "card", "ring", "necklace", "bracelet", "earring", "glasses", "umbrella", "purse"
]
# word_list = ['apple','car','door']
hangman = ['''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']

print("WELCOME TO THE HANGMAN GAME!!!!!!!!!")
print('''  +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========= ''')
game=''
display = []
hold_letter = []
game_over = False
while not game_over:
    word = random.choice(word_list)
    word_len = len(word)
    no_of_guess = 6
    hangman_face = 0
    display = ["_"] * word_len
    hold_letter = []

    print("Your word is : ")
    print(" ".join(display))
    while no_of_guess != 0 and hangman_face < 6:
        print(hangman[hangman_face])
        guess_letter = input("Please Guess a letter: ").lower()
        guess_value = 0
        if guess_letter in hold_letter:
            print("You already guessed that letter.")
        else:
            hold_letter.append(guess_letter)
            for i, x in enumerate(word):
                if guess_letter == x:
                    display[i] = x
                    guess_value += 1
            if guess_value == 0:
                hangman_face += 1
                no_of_guess -= 1
                print(hangman[hangman_face])
            else:
                print(hangman[hangman_face])
        print(f"Your Word to guess is: {' '.join(display)}")
        print(f"You've {no_of_guess} left ")
        if no_of_guess == 0:
            print(f"Your word was {word}")
            print("GAMEEEE OVEERRRR!!!")
            game_over = True
            break
        if '_' not in display:
            print("You win")
            game_over = True
            break
        


    
        
        
                
                
                   
        
    