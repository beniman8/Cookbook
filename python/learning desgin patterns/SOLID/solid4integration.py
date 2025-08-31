# [I]nterface segregation
# it is better to have several interface rather than one interface
# we will add two factor authentication to show an example
# composition is separating the different behavior of a subclass to a class in order to use it later on

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

# This is called using composition instead of us using more subclasses 
class SMSAuth:
    
    authorized = False 
    
    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True
    
    def is_authorized(self)->bool:
        return self.authorized
    
class PaymentProcessor(ABC):
    ''' responsibility is to take care of the payment
        making the payment processor an abstract class 
        helps me leave the code open for extension ex now 
        i can add paypal payment method  , bitcoin payment method 
        without having to change the pay method
    '''
    @abstractmethod
    def pay(self,order):
        pass

#this got replaced with the SMS auth
# class PaymentProcessor_SMS(PaymentProcessor):
#     ''' this is for the payment processor that would need sms verification
#     '''
    
#     @abstractmethod
#     def auth_sms(self,code):
#         pass

# class DebitPaymentProcessor(PaymentProcessor_SMS): this a way to do it
class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self,security_code,authorizer:SMSAuth):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")


# paypal need email and not security code
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address,authorizer:SMSAuth):
        self.authorizer = authorizer
        self.email_address = email_address


    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email_address: {self.email_address}")
        order.set_status("paid")


order = Order()
order.add_item("Car",2500,2)
order.add_item("PC",500,6)
order.add_item("TV",300,8)


print(order.total_price())
authorizer = SMSAuth()
processor = PaypalPaymentProcessor("test@email.com",authorizer)
authorizer.verify_code(24568)
processor.pay(order)
