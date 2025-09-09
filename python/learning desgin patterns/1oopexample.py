############################# GREETING RECIPE/OBJECT  ###########

# Define the greeting class
class Greeting:
    # Constructor for the greeting class 
    def __init__(self, name):
        self.name = name 
        
    # Define our greeting method 
    def say_hello(self):
        #print a personalized greeting message 
        # using the 'name' attribute 
        print(f"Hello, {self.name} !")
        

#inherit everything for greeting
class BetterGreeting(Greeting):
    
    #overwriting say hello from the greeting class
    def say_hello(self):
        print(f"Hello Better {self.name}")


############################# GREETING RECIPE/OBJECT  ###########

# Create an object of the greeting class,
# initializing it with the name 'Jhon'
greeting = Greeting("jhon")
better = BetterGreeting("lisa")

# Call the 'say_hello' method on the 'greeting'
# object to print the greeting message 
greeting.say_hello()
better.say_hello()

