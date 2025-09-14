
class ClassicSingleton:
    # class-level variable to store single class instance 
    _instance = None 

    # override the __init__ method to control initialization
    def __init__(self):
        # raise an error to prevent constructor utilization
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if not cls._instance:#NOTE: lazy instantiation 
            # create new instance of the class
            cls._instance=cls.__new__(cls)
        # return the single instance of the class, either 
        # newly created one or existing one
        return cls._instance


s1=ClassicSingleton.get_instance()

class Singleton:
    # class-level variable to store single class instance 
    _instance = None 

    # override the __new__ method to 
    # control how new objects are created 
    def __new__(cls):
        #check if instance of the class has 
        #been created before. NOTE: lazy instantiation 
        if not cls._instance:
            #create new instance of the class 
            # and store it in _instance
            cls._instance = super().__new__(cls)

        # return the single instance of the class , either
        # newly created one or existing one 
        return cls._instance

s2 = Singleton()


class SingletonMeta(type):
    #dictionary stores single instance of the class for 
    # each subclass of the singleton meta metaclass 
    _instances = {} 
    def __call__(cls, *args, **kwds):
        #Single instance of the class already been created ?
        if cls not in cls._instances:
            # create the instance by calling the call
            # method of the parent's super call
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
            
        return cls._instances[cls]


# our actual singleton class 
class SingletonGreat(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

