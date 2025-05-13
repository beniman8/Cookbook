'''
function can get complicated so  ou want to explain it for your future self

you can either add an explainer text which is called a docstring 

you can also hint at what type of data you expect 
for the parameters and the return value



'''


def test(a:int,b:int) -> int:
    '''A simple function that prints 2 parameters  '''
    print(a)
    print(b)
    
    return a + b
    
test(1,2)


print(test.__doc__)
help(test)