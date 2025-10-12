# American Express
# 378282246310005

# American Express
# 371449635398431

# American Express Corporate
# 378734493671000

# Australian BankCard
# 5610591081018250

# Diners Club
# 30569309025904

# Diners Club
# 38520000023237

# Discover
# 6011111111111117

# Discover
# 6011000990139424

# JCB
# 3530111333300000

# JCB
# 3566002020360505

# MasterCard
# 5555555555554444

# MasterCard
# 5105105105105100

# Visa
# 4111111111111111

# Visa
# 4012888888881881

# python credit card validator


# remove any dashes or spaces
# add all digits in the odd places from right to left
# if result is a two digit number
# add the two digit number together to get a single digit
# sum the totals of steps 2 and 4
# if sum is divisible by 10, the credit card is valid


# credit_card = input("enter your credit card number ")

# dash_filtered = "".join([num for num in credit_card if num !="-"])

# res=[num for index,num in enumerate(dash_filtered) if index %2 ==1]
# res2=[num for index,num in enumerate(dash_filtered) if index %2 ==0]


# r=0
# for val in res:
#     r+=int(val)

# v=str(r)
# f=0 
# if r >= 10:
#     #add two digit to get a single digit
#     f= int(v[0])+int(v[1])

# # sum the two numbers
# two_num = r+f    

# # if sum is divisible by ten
# if two_num %10 == 0:
#     print("valid")
# else:
#     print("not valid")


# tutorial method

# step1
credit_card= input("credit card number ?")
credit_card = credit_card.replace("-","")
credit_card = credit_card.replace(" ","")
credit_card = credit_card[::-1]


# step 2
sum_odd_digits=0
for x in credit_card[::2]:
    sum_odd_digits +=int(x)


# step3
sum_even_digits=0
for x in credit_card[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# step 4 
total = sum_odd_digits + sum_even_digits

#step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
