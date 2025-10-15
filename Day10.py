#for loop

# for i in range(1,11):
#     print(i, end=" ")
    
    
# bag = ["red","green", "blue"]

# for ball in bag:
#     print(ball)
    
# for i in range(1,11,2):
#     print(i, end=" ")


# name="nandan"
# for index, letter in enumerate(name):
#     print(letter*(index+1))
    
# l=[1,2,3,4]
# for index, num in enumerate(l):
#     print(f"{num} is in {index}th index.")
    

# l=[1,2,3,4,5]
# for num in l:
#     print(num)
#     if num == 4:
#         break
# else:
#     print("All printed")
        
        
# d={"name":"nandan", "age":21, "income":10}
# for key, value in d.items():
#     print(key, " ", value)

for i in range(2,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")