'''

python can delete things with del thing

you can delete a whole variable using del 

but most of the time you use del to delete 

values that are inside a list

'''

#delete variable
# a = 1

# del a 

# #NameError: name 'a' is not define
# print(a)


#delete item from a list


a = [1,2,3,4,5]

#del ( removes item by index)

del a[1]

print(a)


#remove item by value 
a.remove(4)

# remove using pop that returns the value that got deleted
a.pop(-3)

# clear the whole list
a.clear()