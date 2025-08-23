'''
A sting is basically a word

you create them with single or double quotation mark ''  ""


string can also be use with math operation 'you' + 'me' 

'''


#quotes for strings
# test_var = 'Test 1'
# test_var2 = "Test 2"
# print(test_var)
# print(test_var2)


# # quotes inside of string must not match the one surrounding the string
# test_var3= 'He said "this was great" '

# #using simple escape character use before a character you want python to read as a character
# test_var4='He said\'This was great\' '


#escape character \n \t \r


# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

# test_var5 ='Line1: some text \nLine 2: some more text'
# print(test_var5)


# #multiple lines

# test_var6 ='''A comment
# another comment
# '''

# print(test_var6)



#math and stings
# test_var7= 'hello'+ " " + 'world'
# test_var8 = 'copy' * 2



#how to get values into strings
# name= "john"
# age = 67

# #using F string
# greeting_string = f"Hello {name}, you are {age} years old"

# #using format
# #greeting_string = "Hello {}, you are {} years old".format(name,age)


# print(greeting_string)



#exercise
#create f string that says: hello, my name is X and my hobby is Y
#X and Y should be separate variables
#the second half of the sentence should also be on a separate line

X='Garry'
Y='fishing'

greeting_string = f'Hello, my name is {X} \nand my hobby is {Y}'




print(greeting_string)