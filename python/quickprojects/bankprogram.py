# this is a bank program   
# show balance 
# deposit money 
# withdraw money 
# exit the program


# show the menu options 

class Menu:
    
    
    def show_menu(self):
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

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
            

# instance of a bank account we can use as demo
bank_account = BankAccount(account_number="123654896",balance=1000)


#program loop 

running = True
menu = Menu()
amount=0


while running:
    
    menu.show_menu()
    selection=input("Please select a number from 1 to 4: ")
    
    if selection == "4":
        running = False
    elif selection == "1":
        print("######################################################################")
        print(f"The balance of your account is $ {bank_account.get_balance():.2f}".capitalize())
        print("######################################################################")
        
    elif selection == "2":
        amount= float(input("how much money do you want to deposit? :"))
        bank_account.deposit(amount=amount)
        print("######################################################################")
        print(f"depositing money $ {amount} in to your account /n")
        print(f"your balance is now $ {bank_account.get_balance():.2f}")
        print("######################################################################")
    elif selection == "3":
        amount= float(input("how much money do you want to withdraw? :"))
        bank_account.withdraw(amount=amount)
        print("######################################################################")
        print(f"you have withdrawn $ {amount} in to from your account /n")
        print(f"your balance is now $ {bank_account.get_balance():.2f}")
        print("######################################################################")
    else:
        print("you have not selected a number on our list")
