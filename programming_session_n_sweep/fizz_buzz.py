# fizz buzz program 
# print every number 1-100 #DONE
# divisible by 3 -> Fizz
# divisible by 5 -> Buzz
# divisible by 15 -> FizzBuzz


for num in range(1,101):
    if num%15 ==0:
        print('FizzBuzz')
    elif  num%3 ==0:
        print('Fizz')
    elif num%5 ==0:
        print('Buzz')
    else:
        print(num)
        