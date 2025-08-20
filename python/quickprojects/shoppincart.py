
class Item:
    
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity
        
        

class Cart:
    
    def __init__(self):
        
        self.items = []
        
        
        
    def add_item(self,item):
        self.items.append(item)
        
    def save_items(self):
        #TODO save item in a text file
        pass
    
    def read_items(self):
        #TODO read items from a text file
        pass
        
    def show_items(self):
        
        for item in self.items:
            print(f"{item.name} {item.price} {item.quantity}")
            
            
print("Enter the items you want in your cart")

running = True

cart = Cart()

while running:
    #gathering data to create the item
    start= input("would you like to add items to your cart (y/n)")
    if start.lower() == "y":
        
        name =input("what is the name of the item you would like to add: ")
        price =input("what is the price of the item you would like to add: ")
        quantity =input("what is the quantity of the item you would like to add: ")
        
        
        item = Item(name,price,quantity)
        
        cart.add_item(item)
        print("------------------------------------------------------------------------")
    else:
        running = False

cart.show_items()
    
    