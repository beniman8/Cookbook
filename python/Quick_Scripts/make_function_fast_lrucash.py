''''
Here we are learning to make a function fast by using LRU_CACHE
Therefor increasing the performance 


in this example we have a recursive function for solving the fibonacci sequence


'''
'''
def fib(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
#this here will start to take long the more it solves th
for i in range(0,40):
    print(f'{i}: {fib(i)}')
    
'''


#here is the improved version that is faster

'''
LRU cash save the result of this function there for stopping
the program from making a new calculation every time it is called 
'''

from functools import lru_cache

@lru_cache
def fib(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
#this will now calculate it instantly
for i in range(0,40):
    print(f'{i}: {fib(i)}')
    
    