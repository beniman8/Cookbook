class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number  # protected attribute (single underscore)
        self.__balance = balance # private attribute (double underscore - name mangling)
        
    # getter method for the private attribute 
    def get_balance(self):
        return self.__balance

    # setter method for the private attribute 
    def set_balance(self,balance):
        if balance >=0:
            self.__balance = balance
        else:
            print("invalid balance")
    
    
    # setter method for the private attribute
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("invalid deposit amount")
            
    # public method that uses the private attribute
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
        else:
            print("Invalid withdraw amount")
            
# Testing the encapsulation 
account = BankAccount("123456",1000)

# accessing the protected attribute (not recommended but possible )
print("Account number: ",account._account_number)

# accessing and modifying the private attribute through getter and setter methods 
print("Initial balance: ",account.get_balance())
account.set_balance(555)
print("updated balance: ",account.get_balance())


# using public methods that internally use the private attribute 
account.deposit(50)
print("Balance after deposit: ",account.get_balance())
account.withdraw(20)
print("Balance after withdrawal: ",account.get_balance())