#Homework

"""1. Lambda Function: Write a lambda function that multiplies two numbers."""

# multi = lambda a, b : a * b
# print(multi(2,3))


"""2. Recursive Function: Write a recursive function that calculates the sum of the first n numbers."""

# def recursion(n):
    
#     if n == 0:
#         return n
#     else:
#         return n + recursion(n-1)
    
# print(recursion(5))


"""3.Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
"""

def average(*n):
    total = sum(n)
    count = len(n)
    avg = total / count
    print("Sum is :",total)
    print("Average is: ",avg)
average(1,2,3,4,5,1)