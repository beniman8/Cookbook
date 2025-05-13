'''
python can open simple file 

ex: txt
'''
#open and close it manually 
file = open('test.txt')
print(list(file))
file.close()


# open and close it automatically
with open('test.txt') as file:
    
    #prints individual characters
    #print(file.read())
    
    for line in list(file):
        print(line)
        
# write some file

# with open('test.txt','a') as file:
    
#     file.write('\nthe next line i wanted to tell you bye')


#exercise 
# create a nre text file and draw a tree in it


with open('tree.txt','w') as file:
    file.write('\n        *          ')
    file.write('\n       ***         ')           
    file.write('\n      *****        ')            
    file.write('\n     ********      ')        
    file.write('\n        *          ')        
    file.write('\n      *****        ') 