# rock paper scissors 

msg = """
1.Rock
2.Paper
3.Scissors

"""

import random

words = ['rock' ,'paper', 'scissors' ]



relationship ={'rock':'scissors','paper':'rock','scissors':'paper'}

running = True 

while running:
    computer_choice = random.choice(words)

    usr_input=words[(int(input(msg)) -1)]

    print(usr_input,computer_choice)

    if computer_choice == usr_input:
        print('Tie Game')
    elif relationship[usr_input] == computer_choice:
        print('You Won ')
    else:
        print("You lost")
