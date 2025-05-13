'''
how to pick multiple element from a list

[1,2.3][start:end:direction/step size]

python goes to the end of the list but does not include it when it returns the value
so start from index 1 to 4 will go to 4 but return index 1 to 3 

list slicing always returns a list even if there is only a single value


'''

my_list = [1,2,3,4,5,6,7,8,9,10]

#default slicing 
default_slicing = my_list[::]

#reverse count with start and end
negative_slicing =my_list[-1:4:-1]

#every second value
skip_step_slicing = my_list[0:4:2]

#reverse the whole list
reverse_slicing =my_list[::-1]

print(skip_step_slicing)

#excercise
# start from 8 and got to 2, pick every second element.

solution = my_list[7:0:-2]

print(solution)
