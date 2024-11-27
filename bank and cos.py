#Bank
class Bank: 
    def __init__(self, name, account_number, ini_balance): 
        self.name = name 
        self.account_number = account_number 
        self.ini_balance = ini_balance

    def deposit(self, amount): 
        if amount > 0: 
            print(f"Your amount {amount} rupees successfully deposited")
            self.ini_balance += amount 

        else: 
            print(f"Your amount {amount} rupees does not get deposited") 

    def withdraw(self, amount): 
        if amount <= self.ini_balance:  
            print(f"Your amount {amount} rupees successfully withdrawn") 
            self.ini_balance -= amount 
        else: 
            print("You don't have sufficient balance in your account") 

    def check_balance(self): 
        print(f"Your remaining balance in the account is {self.ini_balance}") 

holder1 = Bank("Amala", 8945612378, 25000) 
holder1.deposit(8000) 
holder1.withdraw(3000) 
holder1.check_balance()

#cosmetics
class Cosmetics:
    def __init__(self, name="secret",brand="secret",price="secret",category="secret"):
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category
    def display(self):
        print(f"Cosmetic Product Information:")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price} ")
        print(f"Category: {self.category}")


product1 = Cosmetics("Eyelinear","dazler",234,"Eye Makeup")  # Using default constructor
product1.display()
