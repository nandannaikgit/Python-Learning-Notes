# def decorator_name(func):
#     def wrapper():
#         print("Namaskara")
#         func()
#         print("Take care")
#     return wrapper

# @decorator_name
# def intro():
#     print("I am nandan from karnataka")

# intro()


# @decorator_name
# def bye():
#     print("bye")
    
# bye()


def show_result(func):
    def wrapper(a,b):
        print("Result: ", end="")
        func(a, b)
    return wrapper

@show_result
def add(a, b):
    print(a+b)
add(1,2)