# This is a temperature conversion program °F = °C * 9/5 + 32     ////  °C = (°F - 32) ÷ (9/5) 


class Temperature:
    
    def __init__(self,value):
        self.value = float(value)
        
        
    def convert(self,unit):
        
        
        if unit =="f":
            #convert to celsius
            celsius = (self.value-32) / (9/5)
            print(f"your conversion to celsius is {celsius} degrees") 
        elif unit =="c":
            fahrenheit = self.value * (9/5) +32
            print(f"your conversion to fahrenheit is {fahrenheit} degrees") 
            #convert to fahrenheit
        else:
            print("you have not entered anything close to C or F")
        
        
temperature = input("What is the temperature today: ")
unit = input("is it celsius or fahrenheit please enter (c/f)")

temp = Temperature(temperature)
temp.convert(unit)