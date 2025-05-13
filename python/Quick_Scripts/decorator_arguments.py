def decorator(fun):
    
    def wrapper(*args, **kwargs):
        print('the decoration begins')
        fun(*args, **kwargs)
        print('the decoration ends')
    
    return wrapper


@decorator
def function(func_parameter):
    
    print(func_parameter)
    
function('this is america')