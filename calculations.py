def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b

print("1. Addition\n2.Subtraction\n3.Multiplication")
choice = int(input("Enter your choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Addition is ",add(a,b))
    
elif choice == 2:
    print("subtraction is ",sub(a,b))
    
elif choice == 3:
    print("Multiplication is ",mul(a,b))
    
else:
    print("Invalid input!")
