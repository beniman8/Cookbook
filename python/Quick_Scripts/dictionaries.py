'''
is a complex container for other variables 

{'key':'value',1:[1,2,3]}

dictionaries are nothing but organized container where every key gets a value

think about it as a self storage unit that has a key for every unit that needs to be used 
in order to access the value or items that are inside the locker/ storage.

you can not duplicate keys , once you add the same key you are overriding the old one

indexing does not work with dictionary

'''

test_dict = {'car':123,'dog':['woof','meow'],1:True}

print(test_dict['dog'][0])

#basic of dictionary
print(test_dict.values())
print(test_dict.keys())
print(test_dict.items())

#converting dictionary

print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))


#indexing or return a value in the dictionary
print(test_dict['car'])
#get is a bit better because it doesn't crash when it does not get a key
print(test_dict.get('car'))


#Exercise 
# do research and use the update method to add another key value pair

test_dict.update({6:'cat'})
test_dict.update(final='world')
test_dict['E'] = 234
print(test_dict)


