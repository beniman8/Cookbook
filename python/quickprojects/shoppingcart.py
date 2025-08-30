#shopping cart program 


foods = [] 
prices = [] 
total = 0 

shopping=True

while shopping:

    customer_input = input("what foods would you like to buy  (press q to quit) ")
    
    if customer_input.lower() == "q":
        shopping = False
        
    else:
        price = float(input(f"enter the price of {customer_input}: $"))
        foods.append(customer_input)
        prices.append(price)
        
print("--------------- YOUR CART --------------------")
for food in foods:
    print(food, end=", ")
    
for price in prices:
    total += price
    
print(f"Your total for this cart is: ${total}")
