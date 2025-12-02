class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0   #Encapsulation
        
    def check_balance(self):
        print(f"Balance: {self._balance}")
        
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit Sucessfull. Updated Balance: {self._balance}")
        
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw Succesfully. Updated Balance: {self._balance}")
        else:
            print("Balance is not enough.")
            
class SavingsAccount(Account):
    
    def calculate_interest(self):
        interest_rate = 0.04  #4%
        interest = self._balance * interest_rate
        print(f"Interest: {interest}")
        
class CurrentAccount(Account):
    def withdraw(self, amount):
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdraw Succesfully. Updated Balance: {self._balance}")
        else:
            print("Ask is over limit.")
            
            
class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self. __accounts = {}
        
    def create_account(self, id, holder_name, type):
        if type == "savings":
            new_account = SavingsAccount(id,holder_name)
        elif type == "current":
            new_account = CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print("Account creation sucessfull")
        return new_account
    
    def get_account(self, id):
        if id not in self.__accounts:
            print("Account not found!")
            
        else:
            account = self.__accounts[id]
            print(f"\nID: {account.id}\nHolder Name: {account.holder_name}")
            return account
        
n = Bank("Nandan Bank of Karnataka", "Bhatkal")
s1 = n.create_account("1", "Nandan", "savings")
c1 = n.create_account("2", "virat","current")

s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.calculate_interest()