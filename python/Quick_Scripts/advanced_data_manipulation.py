'''

more advanced wat to loop over data 
sorting data 
list comprehension
data handling

'''

#manipulating list and for loops

inventory_names = ['wood','screws','wheels','metal parts','Rubber bits','screwdrivers']
inventory_numbers =[23,45,434,5677,65,67]

#print(list(zip(inventory_names,inventory_numbers)))

#Zip function
for name,number in zip(inventory_names,inventory_numbers):
    print(f'{name} current inventory: {number}')
#Enumerate function 

print('--------------------------------')
#print(list(enumerate(inventory_names)))
for index ,name in enumerate(inventory_names):
    print(f'{name} current inventory: {inventory_numbers[index]}')
    
    
print('--------------------------------')
#exercise
# combine zip and enumerate to get 'Screws [id: 0] - inventory: 43'

for index,inventory in enumerate(zip(inventory_names,inventory_numbers)):
    
    print(f'{inventory[0]}  [id: {index}] - inventory: {inventory[1]}')