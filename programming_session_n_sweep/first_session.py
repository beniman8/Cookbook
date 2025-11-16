# Magic 8 Ball games 
import random

output=['Yes','No','Maybe']

running = True 

while running:
    user_input= input('What is your question? :')
    print(random.choice(output))