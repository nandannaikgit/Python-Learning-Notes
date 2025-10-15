#while loop

#attempts --> iteration


# i=0
# while i<=100:
#     print(f"Try again{i}")
#     i = i + 1
    
    
# is_failed=True
# i=1

# while is_failed:
#     if i%2!=0:
#         i = i + 1
#         continue
#     print(f"Attemot {i}")
#     i= i + 1
#     if i>100:
#         break
# print("I gave Up!")
        
        
# i=0
# while i<=10:
#     print("nandan"*i)
#     i = i + 1
    

# i=0
# while i<=10:
#     x = 0
#     while x<i:
#         print("nandan", end="-")
#         x += 1
#     print("")
#     i = i + 1


pin = "1234"
trials=1
while trials<=3:
    input_pin = input("Trial-{trials} | PIN >>")
    trials += 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")