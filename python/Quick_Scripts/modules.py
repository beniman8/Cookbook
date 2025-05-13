'''
Modules are extra parts that we can attach to our programs

modules are use to add extra functionality in your code

we can install other module made by other people  using pip

python already comes with built in modules

'''
#random module
import random, math
import string
#from math import acos as cos   
#from random import *

import datetime
import pytz

test_list = [2,3,4,5,67]

random_number = random.randint(0,10)

random_choice = random.choice(test_list)


#help(random)
print(random_number)
print(random_choice)
print(string.ascii_letters)
print(math.floor(4.8))
print(datetime.datetime.now())
#print(pytz.all_timezones)

# for zone in pytz.all_timezones:
    
#     print(f'The time in {zone} is {datetime.datetime.now(pytz.timezone(zone))}')