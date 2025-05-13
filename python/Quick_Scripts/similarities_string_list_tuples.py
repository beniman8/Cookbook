'''
strinfs arce actualy very similar to lists and tuples
they are all containers with different formats

'''

test_String = 'this is a test string'
test_list = [1,2,3,4]


# #turning a string into a list / tuple

# print(test_String.split())

#this tries to turn data into a list
# print(list(test_String))

#this tries to turn data into a tuple
# print(tuple(test_String))

#turn a list / tuple into a string the value must be a string in order for this to work
# print('Gap'.join(['one','two']))

#force the numbers to turn into a string by calling the str method and passing the list as an argument
# print(str(test_list))

#indexing on a string work the same thing as list and tuple
# print(test_String[3])

# exercise 
# remove all tje stuff and only print out 1 2 3 4
print(str(test_list).replace('[','').replace(']','').replace(',',''))
print(str(test_list).strip('[').strip(']').replace(',',''))

