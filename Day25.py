# class ATM:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def check_balance(self):
#         print(self.__balance)
        
# cbi = ATM(1000)

# cbi.balance = 10000000000000000

# print(cbi.__balance)



class Database:
    def __init__(self):
        self.storage = {}
        
    def write(self,key,value):
        self.storage[key] = value
        
    def read(self, key):
        return self.storage[key]
        