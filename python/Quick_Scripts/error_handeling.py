'''
your code should not contain any errors 
but sometimes you have no choice cause some program can cause
an error

'''
#anticipating errors / exceptions 
# try:
#     print(a)
#     print(1/0)
# except ZeroDivisionError as e:
#     print('you can not divide by zero',e)
# except NameError as a:
#     print('does not exist',a)
# else:
#     print('something else')
# finally:
#     print('we are done')
    
# #raising exceptions 

# var_must_be_string = 1

# if isinstance(var_must_be_string,str):
#     print(var_must_be_string)
# else:
#     raise TypeError('Must be a string')

# assert only run the code if this is true

# a = 8

# assert a == 5


#exercise
#create a list and try to raise an index error

#also add else and finally

test_list = [1,2,3,4,5]

index_to_print = 4
try:
    print(test_list[index_to_print])
except IndexError as e:
    print('There is no such index in the list',e)
else:
    print(test_list[index_to_print])
finally:
    print('We have finished running the program')