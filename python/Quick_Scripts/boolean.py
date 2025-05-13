'''
Boolean is True or False

usualy created by comparison operator
1) == or equal to 
2) != or not equal to
3) > or greater than
4) >= or greater than or equal to
5) < or less than
6) <= or less than or equal to

strings have methods ex:isnum()

check if we have values in list tuples or dictionaries

compare sets to creat boooleans

create boolean by themselves

bool( can accept any number string type of container and still return a value)

false value in bool function are :
0 or 0.0  int or float
'' emtpty string
[],{},() emptry list ,set, dict or tuple
None absence of value

anything else is truthy

'''


#booolean and number
# print(1 == 1)#True if is equal
# print(1 !=2)#true if is different
# print(1 <= 10)# less than or equal

#using not to reverse any line
# print(not 1 < 10)

#booleans and lists and strings using in and not in

my_list = [1,2,3]
my_tuple = (1,2,3)
my_string = 'hello'


#do i have a 1 in my list
# print(1 in my_list)
# #do i have 2 in my tuple
# print(2 in my_tuple)
# #do i have an e in my string
# print('e' in my_string)

# #is for not in my list
# print(4 not in my_list)

# #is e not in my string
# print('e' not in my_string)


# data conversion exercise
e_dict = {1:'one',2:'two',3:'three'}
#check if the key 1 exists in dict
#check if the value 'four' exists in the dic

key_one_exists= 1 in e_dict
value_4_exists = 'four' in e_dict.values()

print('does value 4 exists: ',value_4_exists)
print('does key 1 exists: ',key_one_exists)


#booleans themselves not True 
#print(True,False)


#bool function
print(bool(2323))
print(bool(0))


print(bool(''))



