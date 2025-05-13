'''
methods are functions that are attached to objects

'string'.method(arguments)

the reason why method exist is because some functionalities should only exist for certain object 

upper function can only be use forw word o strings.. upper is upper case there is no such thing

as an upercase number or symbol

methods always changes a value

methods can aslo be combined

'''

word='tecx'.upper()

print(word)


username = 'JhoN SmIthXD'.title().strip('d')

print(username)

#find all the methods available for your object
print(dir(username))

# change soda to water
exercise_string = "I like to drink soda".replace('soda','water')

print(exercise_string)