'''
Decorators are function that decorates other functions 
what we are doing is wrapping a function on top of another function
def func():

decorator func()
func():


test your code without changing 

you want to avoid making unnecessary changes

decorator allows you to use code in classes when an attribute is changed
'''

def func():
    print('function')
    
def wrapper(func):
    print('hello')
    func()
    print('goodbye')


def another_function():
    
    def new_func():
        print('new function')
    
    return new_func

#wrapper(func)


new_fun = another_function()

new_fun()