'''
combine simple python tools such as variables  , loops to creat e
more complex systems


functions are a block of code that can be reused


def function_name():
    do something  
    
'''

#creating a function
def test_function():
    print('hello')
    test = 1 + 2
    print(test)
    
    
#calling the function   
test_function()  


def calcultator(num1,num2):
    result = num1 + num2
    
    print(result)
    
    
#exercise calculator that take a third argument as an arithmetic operation

def better_calculator(num1:int,num2:int,operation:str) -> str:
    
    if operation.lower() == 'plus':
        print(num1+num2)
        
    elif operation.lower() == 'minus':
        print(num1-num2)
        
    else:
        print('I do not understand your operation')
        
better_calculator(2,8,"minus")