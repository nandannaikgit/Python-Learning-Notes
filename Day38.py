def decorator_name(func):
    def wrapper():
        print("Namaskara")
        func()
        print("Take care")
    return wrapper

@decorator_name
def intro():
    print("I am nandan from karnataka")

intro()


@decorator_name
def bye():
    print("bye")
    
bye()