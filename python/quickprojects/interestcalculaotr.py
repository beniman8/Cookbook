# python interest calculator time is in years


principal = 0
rate =0
time=0


while principal <= 0:
    principal =float(input("how much is your initial principal balance: "))
    if principal <= 0:
        print("principal can not be less than or equal to zero")
while rate <= 0:
    rate =float(input("how much is your interest rate: "))
    if rate <= 0:
        print("rate can not be less than or equal to zero")
while time <= 0:
    time =int(input("how many years: "))
    if time <= 0:
        print("time can not be less than or equal to zero")
        
        
total = principal * pow((1+rate / 100),time)

print(f"balance after {time} year/s: ${total:.2f}")