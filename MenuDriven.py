def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b


print("-----  Simple Calculator ------")
print("1. Addition")
print("2. Subtraction")
print(". Multiplication")
print("4. Addition")
print("5. Exit ")

choice = int(input("Enter your choice: "))

if choice in {1,2,3,4}:
    a = int(input("Enter First number: "))
    b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(a,b))
    
elif choice == 2:
    print("Result:", sub(a,b))
    
elif choice == 3:
     print("Result:", mul(a,b))
     
elif choice == 4:
     print("Result:", div(a,b))
     
elif choice == 5:
    print("Quitting....")
    
else:
    print("Invalid choice. Tyr again!!")
    
