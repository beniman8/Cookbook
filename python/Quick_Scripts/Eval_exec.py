'''
Eval and exec translate strings into python code

Eval('1+1') returns 1+1  
'''

print(eval('1+1'))
print(eval('"test".upper()'))

exec('if True:print("oh lord")')
exec('a=10')
#print(a)

my_string = 'test what up'
functions = ['upper()','title()','lower()','casefold()']
for func in functions:
    print(eval(f'my_string.{func}'))