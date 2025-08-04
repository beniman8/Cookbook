# This is a todo list python program that allows you to add and delete stuff on your list 
# we will use a txt file to store the things on the list 



print("Welcome to your to do list program \n")
print("Please enter the name of the things you want to add on your to do list  \n")
print("Write 'exit' to stop the program  \n")
print("Write 'delete' to delete content on your list  \n")
print("Write 'show' to see the content on your list  \n")




running = True 

while running:
    
    things = input("add stuff here : ")
    
    if things == 'exit':
        running = False
        
    elif things == 'delete':
        open('todo.txt','w').close()
    
    elif things == 'show':
        with open('todo.txt') as f:
            for line in list(f):
                print(line)
    elif things != '':
        with open('todo.txt','a') as file:
            file.write(f"\n {things}")
        
