'''
#whne you creat a function you give it paramaters you can work with 

those paramater can now be use as variables inside the function
def test(paramater,paramter)
    do something
    
# when you call an function you pass down an argument to it in order for it to do something  
test(argument,argument)


'''


# arg 4 has a default arguments
def test_function(arg1,arg2,arg3,arg4='default'):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

# positional arguments
test_function(1,'2',False,[1,'test',True])

# keyword arguments
test_function(arg1=3,arg2='Hey',arg3=True,arg4=(1,2,3,4))

# positional arguments alwasy come before keyword arguments
test_function(3,'Hey',arg3=True,arg4=(1,2,3,4))


# exercise
# create greter function with 3 parameters: person , gret and weekday
# person and greet should have default arguments ('Person' for person and 'Hello' for greet)
# inside of the function use an f-string to print the greet and the person and also print the weekday
# when calling the function, use at least one positional argument and 1 keyword argument

def greetings(weekday,person='Person',greet='Hello'):
    
    print(f'{greet}, {person} happy {weekday}')

greetings('monday',person='Sidney')


'''
if you do not knw the number of arguments


list unpacking using * before the argument
turns all the arguments passed down to a tuple that can be looped

keyword unpacking  by using ** befor argumets 

this will look for all the keyword and arguments and unpack them into a dictionary

'''

def print_all(*args):
    print('all')

def print_evrything(*args, **kwargs):
    
    print(args,kwargs)


print_evrything(1,2,3,4,['test'],greet='hello')


# exercise
# create a calculator function that prints the sum of an unlimited amount of numbers


def sum_all(*args):
    result= 0
    for number in args:
        result+=number
    print(result)

sum_all(1,2,3,4,5,6,7,8,8,9,54,4)
