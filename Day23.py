# class Human:
#     def __init__(self, name):
#         self.name = name
        
#     def walk(self):
#         print(f"{self.name} is walking.")
        
# nandan = Human("nandan")
# nandan.walk() 


# Homework

"""1 Create a class:
  Write a class mobile with attributes brand and price
  Create two objects of the class and display their attributes using method
  """
  

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
        
#     def display(self):
#         print(f"Mobile brand is {self.brand} and price is {self.price}")
        
# M = Mobile("Motorola", 18000)
# V = Mobile("Vivo",15000)

# M.display()
# V.display()
        
  
"""2.Method Definition:

 Define a class Student with attributes name and marks.
Write a method display_info() that prints the student's name and marks.
Create multiple objects of the Student class and call the method on each.

"""

class Student:
    
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def display_info(self):
        print(f"student name is {self.name}  and marks is {self.marks}")
        
a = Student("nandan",99)
b = Student("praddep",88)
c = Student("divakar",90)

a.display_info()
b.display_info()
c.display_info()