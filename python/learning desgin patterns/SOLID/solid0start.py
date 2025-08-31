# [S]ingle responsibility 
# [O]pen/closed 
# [L]iskov substitution 
# [I]nterface segregation 
# [D]dependency inversion 


class Order:
    items = [] 
    quantities = [] 
    prices = [] 
    status = "open"
    
    
    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0 
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
            return total
        
    def pay(self,payment_type,security_code):
        if payment_type =="debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid" 
        elif payment_type =="credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid" 
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Car",2500,2)
order.add_item("PC",500,6)
order.add_item("TV",300,8)


print(order.total_price())
order.pay("debit","0321547")