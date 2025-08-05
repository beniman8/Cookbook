## this is a simple calculator program 



first_number = str(input('the first number: \n'))

operation = str(input("Enter the operation +,-,*,/ \n"))

second_number = str(input("the second number: \n"))



answer =eval(f'{first_number} {operation} {second_number}')

print(answer)