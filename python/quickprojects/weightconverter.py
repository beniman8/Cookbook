#  1 kilogram = 2.20462 lbs  pounds
#ask if they will be entering their weight in kg or lbs
#if it is in kg we output the value in lbs
#if it is in lbs we output the value in kg 


class WeightConverter:
    
    def __init__(self,weight):
        self.weight = weight
        
        
    def convert(self,unit):
        
        if unit == "lbs":
            kg = float(self.weight) / 2.20462 
            print(f"your weight in kg (kilograms) is {kg}")

        elif unit == "kg":
            lbs = float(self.weight) * 2.20462 
            
            print(f"your weight in lbs (pounds) is {lbs}")
            
        else:
            print("you have not entered the proper unit value")
            

weight = input("please enter your weight: ")
print("-----------------------------------------------")
unit = input("is the weight you entered in kg or in lbs: ")

converter = WeightConverter(weight)
converter.convert(unit)


