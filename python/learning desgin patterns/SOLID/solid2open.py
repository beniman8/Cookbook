# [O]pen/closed
# we want code that is open for extension so we could extend code with new functionality
# we also want the code to be closed for modification .. no need to modify it

from abc import ABC, abstractmethod


class Order:
    ''' Responsibility is to take care of the order'''
    items = [] 
    quantities = [] 
    prices = [] 
    status = "open"
    
    
    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def set_status(self,result):
        self.status = result
        
        
    def total_price(self):
        total = 0 
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
            return total


class PaymentProcessor(ABC):
    ''' responsibility is to take care of the payment
        making the payment processor an abstract class 
        helps me leave the code open for extension ex now 
        i can add paypal payment method  , bitcoin payment method 
        without having to change the pay method
    '''
    @abstractmethod
    def pay(self,order,security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")


class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")
        
        
class PaypalPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")


order = Order()
order.add_item("Car",2500,2)
order.add_item("PC",500,6)
order.add_item("TV",300,8)


print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order,"21855")
