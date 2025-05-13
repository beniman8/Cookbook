'''
run code for every item inside of a container

for x in [1,2,3]:
    print('12')


for cyclse over every item in the list

and stores the value in x and can treat it like a variable

break and continue also works with a for loop
'''

basic_list = [1,2,3]
basic_tuple = (1,2,3)
basic_dict = {1:'one',2:'two',3:'three'}
basic_set = {1,2,3}
basic_string = 'One two three'
basic_num = 3

# for x in basic_list:
#     print(x)
    
# for x in range(basic_num):
    
#     print(x)
    
    
#exercise 
paractice_list =[[10,40,20,50],[2,42,10],[101,10,4]]
#use a for loop to only print he numbers below 50
# skip values below 10
# end the entire lop if a vaue is above 100


for values in paractice_list:
    
    for value in values:
        if value > 100:
                break
        if value < 50 and value >= 10:
            print(value)
            
            