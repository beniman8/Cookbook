"""
both lists and tuples can be unpacked
a,b =[0,5]
a,b =(0,5)
a=0 , b= 5

you must have the same number of variable as values in the tuple/list in order for unpacking to work

a_list = (1,2,3) is the same thing as a_list = 1,2,3   these are both tuples

"""

a, b = (10, 5)

print(a)
print(b)


c, d = [34, "test"]

print(c)
print(d)

health, energy, weapon = 100, 50, "sword"

print(weapon)

# excercise
value_1 = 10
value_2 = "test"

# switch the value of these two variables
value_1, value_2 = value_2, value_1

print(value_1)
print(value_2)
