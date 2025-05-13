'''

lambda are single line functions

lambda parameter:expression
lambda x:x+1


the result in a lambda is returned automatically


'''


a = lambda x:x+1
simple_calculator=lambda a,b:a+b
print(a(10))
print(simple_calculator(10,20))


# some functions want other functions as arguments
# sort([1,2,3,4,5],function)


#graphical user interfaces

#exercise
#create a lambda function that accepts 1 integer as an argument
# if the integer is > 5 return 'Hello"
# otherwise return bye

result = lambda x:'Hello' if x > 5 else 'Bye'

print(result(6))