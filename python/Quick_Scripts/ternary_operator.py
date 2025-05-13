'''
the different ways your code can be written


True value if expression else False value

'''

x=5 
color=''

if x <5:
    color= 'blue'
else:
    color='red'
    
    
#this is a ternary operator
# i want the color green if x iis les than 7 else i want to color red
color='green' if x <7 else 'red' 
print(f"The color is {'green' if x <7 else 'red'}")
a = ['green' if x <7 else 'red','yellow','orange' ]