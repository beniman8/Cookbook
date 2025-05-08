'''

a python identifier is a name use to identify a variable,function,class,module or other object.

the rules of naming the identifier are:

it starts with a letter A to Z or a to z or an underscore _

followed by zero or more letters , underscores and digits

python does not alow characters such as &comma ;,$ and % within identifier 


python is a case sensitive language so This and this are two different identifiers 

in python

name conventions:

when your identifier name has more than two word us an underscore to separate them.
this is called snake Case 

ex:user_name

the class name start with upper case letters, every other identifier start with lower case
letters 

starting an identifier with single underscore means that the identifier is private
and if you double the underscore you double the privacy

and if it end with two underscores it means it a language define special name
'''


#example 1  using variables:

#valid variable names 
user_name = "Jhon"
age = 24
_count =20
MAX_VALUE=523

#Invalid variables names 

'''
1user = "pop"
user-name="lisa"
if = True  # trying to use a reserver key word won't work

'''


#example 2 classes:

class Something():
    pass





