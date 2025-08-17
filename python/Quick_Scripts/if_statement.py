'''
only run the code if the condition is True

it is always looking for a boolean value
can be extended with elif and else


and condition can be combined
'''

#print(3>4)

#run some code if athe value in a variable is greater than 10
x = 5

if x > 10:
    print('hello')
elif x == 5:
    print('it is 5')
else:
    print("not True")
    

if 1 in [1,2,3]:
    
    print('yes it is')

#excercise
money_available= 100
#if money is greater or equal han 80 - > eat something fancy
#if money greater than 45 -> eat something nice
#if money grgeater than 15 - > eat something okay
#else eat something cheap


if money_available >= 80:
    print('Eat something fancy')
elif money_available > 45:
    print('Eat something nice')
elif money_available > 15:
    print('eat something ok')
else:
    print('eat something cheap')
    
