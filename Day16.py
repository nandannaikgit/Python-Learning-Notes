# def greet():
#     print("Hello, Good Morning!")

# greet()
# greet()
# greet()
# greet()
# greet()


# def marriage(boy,girl):   #parameters
#     print(f"Boy is {boy}")
#     print(f"Girl is {girl}")
#     print(f"{boy} married {girl}")
# marriage("Nandan","Sinchana") # positional arguments
# marriage(boy="Chandan", girl="Sneha") # keyword arguments 
 
 
# tables using function

# def table(num):
#     for i in range(1,11):
#         print(f" {num} * {i} = {num*i}")
        
# table(12)


# def marriage(boy,girl="girl"):   # default parameters
#     print(f"Boy is {boy}")
#     print(f"Girl is {girl}")
#     print(f"{boy} married {girl}")

# marriage(boy="Chandan") # keyword arguments 



# returning values from a function 
# def func(num):
#     return int(str(num)*3)
    
# a=100
# b = func(1)

# c = a + b
# print(c)


# local and global variable

def func():
    x="nandan"  #local variable
    print(x)
    print(y)
y="chandan" #global variable
print(y)
func()
