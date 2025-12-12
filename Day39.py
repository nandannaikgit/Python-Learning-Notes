"""map function"""

# nums = [1,2,3,4,5]

# res = []
# for num in nums:
#     res.append(num*2)
    
# print(res)


# nums = [1,2,3,4,5]

# def double(x):
#     return x*2

# res = list(map(double, nums))
# print(res)


# nums = [1,2,3,4,5]
# res = map(lambda x: x*3, nums)
# print(list(res))


"""Filter function"""

# nums = [1,2,3,4,5]

# def is_even(x):
#     return x%2==0

# res = filter(is_even, nums)
# print(list(res))


# nums = [1,2,3,4,5]
# res = filter(lambda x: x%2!=0, nums)
# print(list(res))


"""Reduce function"""

from functools import reduce

nums = [1,2,3,4,5]

def add(a,b):
    return a+b

res = reduce(add, nums)
print(res)