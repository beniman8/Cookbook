'''

list and tuples are simple data containers

both can contain any kind of data 

strings,numbers,booleans, other lists/tuples and more

tuple  -- (1,'test',True,('other tuple'))

List -- [2,'test2',True,['another list']]

The difference between the two is that tuple is immutable . it means it can not be change.


python assignes a list or a tuple and index number starting with index 0
[1,2,3,4][1] returns second item in list

strings can also use index
'''

#list
my_list =['1',2,4.6,'test',['test']]

# print(my_list)

# #method in list that clears the whole list
# my_list.clear()

# #reverse the list 
# my_list.reverse()

# #append adds to the end of the list
# my_list.append(23)

# print(my_list)

#tuple

my_tuple = (1,4.5,[1,2,3],'test')

# print(my_tuple)

#how to pick elements from a tuple or a list -> indexing or slicing
print(my_list[3])
print(my_tuple[2][1])
#go at the oposit direction of the list
print(my_list[-1])

# exercise
#get the word / string 'hello :)'

excercise_list = ['first entry',[123,456,[0,'Hello :)']], 'bye']
solution = excercise_list[1][2][1]
print(solution)