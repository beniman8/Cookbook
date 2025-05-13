"""
you can pass function into another function as an argument

sorted(iterable,function)


map and filter can also be use ti sort thing but they are being replaced by list comprehension


"""

list_1 = [3, 6, 4, 9]

print(sorted(list_1, reverse=True))


list_2 = [("a", 3), ("z", 10), ("c", 6), ("d", 5)]


def sort_func(item):
    return item[1]


print(sorted(list_2, key=sort_func))

print(sorted(list_2, key=lambda item: item[1]))


# exercise

inventory_names = [
    "wood",
    "screws",
    "wheels",
    "metal parts",
    "Rubber bits",
    "screwdrivers",
]
inventory_numbers = [23, 45, 434, 5677, 65, 67]

combined_list = list(zip(inventory_names, inventory_numbers))
# [('wood', 23), ('screws', 45), ('wheels', 434), ('metal parts', 5677), ('Rubber bits', 65), ('screwdrivers', 67)]
print(combined_list)

# sort list by inventory number
print(sorted(combined_list, key=lambda inventory: inventory[1]))
# sort list by length of the inventory name
print(sorted(combined_list, key=lambda inventory: len(inventory[0])))


# map-changes values with a function inside of a iterable


def power_function(item):
    return item**2


print(list(map(power_function, list_1)))

print(list(map(lambda item: item**2, list_1)))


# filter - filter out values for a condition
def get_below_4(num):

    if num < 4:
        return True
    else:
        return False


print(list(filter(get_below_4, list_1)))
print(list(filter(lambda num: True if num < 4 else False, list_1)))
print(list(filter(lambda num: num < 4, list_1)))

#exercise 
#convert the power and list function to a list comprehension

conv_power =[num**2 for num in list_1]

print(conv_power)

conv_filter =[num for num in list_1 if num <4]

print(conv_filter)