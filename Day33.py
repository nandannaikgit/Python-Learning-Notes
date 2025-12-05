# Errors and exception handling


a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    print(a/b)
except Exception as e:
    print(f"Error : {e}")
else:
    print("Yenu error barlilla")
finally:
    print("Program ended!")