"""variable length arguments *args
                or
    Arbitrary Arguments ( args ,  *kwargs )


"""
""" args  (Multiple Positional Arguments)"""

# def add(*a):
#     print(a)
# add(1,2,3)


# def add(*numbers):
#     return sum(numbers)
# print(add(1,100,2))


"""*kwargs  (Multiple Keyword Arguments)
Allows passing multiple keyword arguments as a dictionary"""
# **kwargs
# def student_info(**details):
#     for key, value in details.items():
#         print(f"{key}: {value}")
        
# student_info(name="Nandan", age=21, course="Python")



# lambda or anonymous function

# def add(a,b):
#     return a+b  #this is normal function

# add = lambda a,b : a + b
# print(add(1,2))

# double = lambda x : 2*x
# print(double(100))


# students = [
#     {"name":"nandan", "marks":10},
#     {"name":"pradeep", "marks":100},
#     {"name":"divakar", "marks":50},
# ]
# students.sort(key = lambda x: x['marks'], reverse=True)
# print(students)


# Recursion : function call itself
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(3))


# Nested function
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()
outer_function("Nandan")
