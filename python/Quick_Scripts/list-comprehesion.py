'''
list comprehension is a way of creating a list using only one line of code

it is one of the most powerful features in python 

you can create simple lists and also you can manipulate existing list with it.

regular way 

my_list = []
for num in range(0,100):
    my_list.append(num)
    
    
list comprehension method

my_list = [num for num in range(0,100)]


you can combine list comprehension to a ternary operator

my_list = [num for num in range(0,100) if num < 10]
my_list = [num if num < 10 else 0 for num in range(0,100) ]

you could use it to filter other lists


comprehension can also be used in dictionaries and sets and tuple

dict_comp = (num:num for num in range(10))
set_comp = {num for num in range(10)}
tuple_comp = tuple(num for num in range(10))

'''

#regular list creation
my_list = []
for num in range(0,100):
    my_list.append(num)


#list comprehension method
my_list2 = [num for num in range(0,100)]

print(my_list)

print(my_list2)

#list comprehension and ternary operator
my_list3 = [num for num in range(0,100) if num < 30]
my_list4 = [num if num < 30 else 'o' for num in range(0,100) ]

print(my_list3)


inventory_names = ['wood','screws','wheels','metal parts','Rubber bits','screwdrivers']
inventory_numbers =[23,45,434,5677,65,67]

replenished__list=[(name,number) for name,number in zip(inventory_names,inventory_numbers) if number <100]

print(replenished__list)

#combined list comprehension

# combine_comprehension =[[(x,y) for x in range(5)] for y in range(10)]

# for row in combine_comprehension:
    
#     print(row)
    
#exercise 
#create the fields for a chess board

#chess_letters = ['a','b','c','d','e','f','g','h']
chess_letters ='abcdefgh'
#mine
chess_board =[[(x,y+1) for x in chess_letters] for y in reversed(range(len(chess_letters)))]
#his
chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]

for row in chess_board:
    
    print(row)
#set comprehension 
set_comp = {num for num in range(10)}
print(set_comp)

#dictionary comprehension
dict_comp ={num:num**2 for num in range(10)}
print(dict_comp)

#tuple comprehension
tuple_comp = tuple(num for num in range(10))

print(tuple_comp)

#Exercise
#create a dictionary with the keys 'A', 'B' , 'C' , 'D' and  'E'
# each key should have a list as value withe the values [1,2,3,4,5]

dict_exercise ={key:[1,2,3,4,5] for key in 'ABCDE'}

print(dict_exercise)