'''


sets are simple container for other variables
{1,'test , True}

sets do not have keys they only have values
every single value in a set must be unique
any duplicates will be deleted

indexing and slicing does not work on sets

set are actualy use for comparison

'''

my_set = {1,2,2,3,4,5}#duplicated value will be eliminated


#use methods to add in set
my_set.add(7)
print(len(my_set))
print(my_set)

#return the first item from the set and remove it from the set
#print(my_set.pop())

#exercise
#use type conversion to get one item from the set by index

set_to_list = list(my_set)

print(set_to_list[2])

#comparison operators

set1={1,2,3,4,4}
set2 =  {4,5,6,7}

#merge 2 set togheter
print(set1.union(set2))
print(set1 | set2)# this will work also


#find the shared value between the two sets
print(set1.intersection(set2))
print(set1 & set2)# this will work also


print(set1.difference(set2))
print(set1 - set2)# this will work also


#exercise

test_list = [43,35,324,234,5,2,32423,542,534,324,23,54,65,323,42,4,123,123,5,1,321,3124,123,123,124,1,31,23,145]
#check if this list has duplicate values
print(len(test_list))
solution = len(set(test_list))

#or

print(len(test_list) == len(set(test_list)))

print(solution)