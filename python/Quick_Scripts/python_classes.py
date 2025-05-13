'''
Everything in python is an object

including strings integer 

function  ->     lent('test')
method ->  'test'.upper()
'''

test = 'what'
print(dir(test))

'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

def test1():
    pass 

print(dir(test1))

'''

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
'__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__',
'__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''



def add(a,b):
    return a + b 

class Test:
    
    def __init__(self,add_function) -> None:
        self.add_function = add_function
        
lest = Test(add_function=add)

print(lest.add_function(2,5))


#exercise 

#create a Monster class with parameter called func, store this func as parameter

# create another class called Attacks , that has 4 methods:
#bite,strike,slash,kick   each method just prints some text

# create a monster object and give it one of the attack methods from the attack class

class Monster:
    
    def __init__(self,func) -> None:
        
        self.func = func 

class Attacks:
    def __init__(self) -> None:
        pass 
    
    def bite(self):
        print('bite') 
    def strike(self):
        print('strike') 
    def slash(self):
        print('slash') 
    def kick(self):
        print('kick')  

attacks = Attacks()     
monster = Monster(func=attacks.bite)

monster.func()
