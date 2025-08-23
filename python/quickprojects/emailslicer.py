email = input("what is your email: ")

index = email.index("@")

username = email[0:index]
site = email[index+1:len(email)]

print(username,site)