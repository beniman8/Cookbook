# creating a concession program to practice using dictionaries

items = {
    "popcorn": 5,
    "hot dog": 2,
    "giant pretzel": 4,
    "asst candy": 1,
    "soda": 1,
    "water": 1,
    
}


class Order:
    items = [] 
    quantities = []
    prices = [] 
    
    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        
        return total

class ShowMenu:
    
    def __init__(self,items:dict):
        self.items = items
    
    def show(self):
            
        print("------------------------------------")
        print("Here is a list of items available to buy")
        for item in self.items.items():
            name = item[0]
            price= item[1]
        
            print(f"name: {name}............price: ${price}")        


###############################The program ##################################
order = Order()
menu = ShowMenu(items)
taking_order = True 


while taking_order:
    
    menu.show()
    
    costumer_input = input("what is the name of the item you would like to order?: ")
    if costumer_input.lower() == "q":
        taking_order = False
        
    else:
        quantity = int(input("How many?: "))
        name = costumer_input
        price = items.get(costumer_input)
        
        order.add_item(name,quantity,price)

print("*******************************************************************")
print(f"the total of this order is : ${order.total_price()}")
