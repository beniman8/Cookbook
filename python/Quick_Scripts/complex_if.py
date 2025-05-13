'''
if statement can be combined or nested  wich help you creat complex systems

and or is use in order to do that


if 5 , 1 and 'e' in 'hello' or 10 != 4:
    do something
    
nesting if statement looks like this . it can go on forever
if a in [a,b]:
    do something
    if 6 <6:
        do something
        if True:
            do something
        
'''

if True:
    print('True')
    
#will never run 
if True and False:
    print('true')
    
if True or False:
    
    print('one of them is true')
    
if True and True and True or True:
    print('all the ands are true and maybe after the or is true')
    

#exercise

money_available = 100 
hungry = True 
bored = True 
#check if money available > 80 and if hungry is true or if bored

if money_available > 80 and hungry == True or bored == True:
    print('Eat something fancy')
    
#nesting if statements
x = '1'
if x in ['a','b','1']:
    print('a is in the list')
    if x.isalpha():
        print('it is a letter')


#exercise
# if you have enough money and you are hungry and bored print eat something fancy
if money_available > 80:
    print('i have enough money')
    if hungry == True:
        print('and i am hungry')
        if bored == True:
            print('Eat something fancy')
        
    



