# num = int(input("Enter num: "))

# match num:
#     case 1:
#         print("one")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("four")
#     case _:
#         print("some other number")
        
        
# day = "Sunday"

# match day:
#     case "Monday":
#         print("start of the work week.")
#     case "Friday":
#         print("Almost weekend!")
#     case "Saturday" | "Sunday":
#         print("It's the weekend!! ")
#     case _:
#         print("Just another weekday.")
            
            
time = 17

is_hungry = False

match time:
    case 9:
        print("breakfast")
    case 14:
        print("Lunch")
    case 17 if is_hungry:
        print("Snacks")
    case 20:
        print("Dinner")
    case _:
        print("work")