"""validate a username 

1. username is no more than 12 characters 
2. username must not contain spaces 
3. username must not contain digits 

"""

class Validate:
    
    def __init__(self,username):
        self.username = username
        
        
    def is_valid(self)->bool:
        characters = True if self.username.__len__() <= 12 else False
        no_space = True if " " not in self.username else False #self.username.find(" ") will also work
        no_digit = True if  self.username.isalpha() else False
        
        

        if characters and no_space and no_digit:
            print("your username is valid")
            
            return True
        else:
            print("your user name is not valid")
            return False
            
        
        
    



username = input("what is the username: ")

validate = Validate(username)

validate.is_valid()
