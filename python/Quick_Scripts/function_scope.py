'''
variable inside a function are only available inside that function

aka a local scope 

outside the function is called a global scope


functions are supposes to be separated from the rest of the code


local scope inside a function helps to keep us organized


Rules of scope

Every function has its own local scope and ever local scope is separate

Global variables can be accessed in the local scope but they cannot be changed or created

you can move between scopes with parameters , global and return  .. but only when needed

'''

#global variable
a = 19 

def test_func():
    # error local variable 'a' referenced before assignment
    # a +=2 
    
    # be only exist inside this function
    b = 4  
    print(a)
    
    #this is another way to get a global variable in a function not really good
    global d 
    
    # the value of None is available global because it returns it
    return None
    
    
test_func()


#exercise 
# create 2 global variables called 'multiplier and has_calculate should be set to the boolean False

# then create a function called multiply_calculator that takes one arguments and calculates
# the multiplication of that number
# inside of the function multiply the parameter with the global variable multiplier
# once the calculation is done set has_calculated to True
# store that new number a variable called result and return it
# print the return value of the function (after it was called with the number )

multiplier =2
has_calculated = False

def multiply_calculator(number:int) -> bool:
    global has_calculated
    result = number * multiplier
    has_calculated = True  
    return result


print(multiply_calculator(2))


