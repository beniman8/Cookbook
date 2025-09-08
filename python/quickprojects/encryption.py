import random       
import string 

chars = " "+string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print("Do not share the key with anyone \n")
# print(f"here is the key for this encryption: {key}")


#Encrypt 

plain_text = input("Enter a message to encrypt: ")
cipher_Text = ""


for letter in plain_text:
    index = chars.index(letter)
    cipher_Text += key[index]
    


print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_Text}")


#DEcrypt 

cipher_Text = input("Enter a message to encrypt: ")
plain_text = ""


for letter in cipher_Text:
    index = key.index(letter)
    plain_text += chars[index]
    


print(f"your encrypted message: {cipher_Text}")
print(f"original message: {plain_text}")
