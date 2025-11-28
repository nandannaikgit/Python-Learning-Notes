# class ATM:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def check_balance(self):
#         print(self.__balance)
        
# cbi = ATM(1000)

# cbi.balance = 10000000000000000

# print(cbi.__balance)



# class Database:
#     def __init__(self):
#         self.__storage = {}
        
#     def write(self,key,value):
#         self.__storage[key] = value
        
#     def read(self, key):
#         if key in self.__storage:
#             print(self.__storage[key])
#         else:
#             print("DB item not available")
        
# db = Database()
# db.write("subscriber","100k")
# db.write("name", "nandan")
# db.read("nandan")
    
    
    
    
#Assignment
"""
1.Encapsulation:

Create a BankAccount class with private attributes for account_number and balance.
Add methods to check balance, deposit, and withdraw funds.
Try accessing the balance directly and observe the result.

"""

class BankAccount:
    def __init__(self, acc_number, balance):
        self.__acc_number = acc_number
        self.__balance = balance
        
    def check_balance(self):
        print(f"Balance is {self.__balance }")
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds.")
        self.__balance += amount
        print(f"Withdraw Successfully - Balance: {self.__balance}")
      
a = BankAccount(1, 100)
a.check_balance()
a.deposit(100)
a.check_balance()
a.withdraw(100) 
a.check_balance() 
a.withdraw(10000) 
a.check_balance
        
    