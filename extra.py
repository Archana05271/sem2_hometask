#3
a= input()
words = a.split()
b= len(words)
print(b)
#4
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10  
    num = num // 10    
print(sum)
#5
sen = input("Enter a sentence: ")
word = len(sen.split())
print("Number of words:", word)
#7
class BankAccount:
    def __init__(self, ini_balance=0):
        self.balance = ini_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        return self.balance
account = BankAccount(100)  
account.deposit(50)
account.withdraw(30)        
print(f"Current balance: {account.get_balance()}")
#8
import re 
email=input("Enter the email id:") 
ex= ex=r'^[a-z0-9._%+-]+@gmail\.com$' 
if re.match(ex,email): 
    print("Valid") 
else: 
    print("invalid")
#9
num=input("Enter the text") 
phone=[] 
for i in num:
    if i.isdigit()==True:
        phone.append(i)
    for i in phone:
        print(i,end="")
#10
import re 
sen=input("Enter the text:") 
ex=r'#\w+' 
output=re.findall(ex,sen) 
print(output)
#2
num = [10, 20, 20, 30, 40, 10, 50, 30]
uni_num = list(set(numbers))
uni_num.sort(reverse=True)
print("Sorted list without duplicates:", uni_num)
#1
#6



