import random

from nltk.corpus import words

# Get the list of English words from the NLTK corpus
english_words = words.words()

# Select a random word from the list
random_word = random.choice(english_words)

# Print the random word
#print(random_word)

running = True

while running:
    print(random_word)
    print(f'the first letter is: {random_word[0]}')
    print(f'the last letter is: {random_word[len(random_word)-1]}')
    guess = input()
        
    if str(guess) == 'stop':
        running = False
        
    elif str(guess) == random_word:
        print('Great')
        random_word = random.choice(english_words)
    else:
        print('wrong try again')
