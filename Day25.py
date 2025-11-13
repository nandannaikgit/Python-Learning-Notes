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
        self.__storage = {}
        
    def write(self,key,value):
        self.__storage[key] = value
        
    def read(self, key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item not available")
        
db = Database()
db.write("subscriber","100k")
db.write("name", "nandan")
db.read("nandan")
    