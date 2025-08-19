
print("Here is the mad libs we are going to complete today\n please enter 5 words in order to complete the game")

print("When I Was Younger I use to ___ at school.")
print("that was one of my favorite ___ to do.")
print("my best friend _____ always ___ to ____ to the mall.")


words=[]

size=5
while(len(words)<5):
    word= input()
    words.append(word)
    

print(f"When I Was Younger I use to {words[0]} at school.")
print(f"that was one of my favorite {words[1]} to do.")
print(f"my best friend {words[2]} always {words[3]} to {words[4]} with me at the mall.")
    


#TODO upgrade this game so that you get prompted when to enter an Noun,Adjective or a Verb
