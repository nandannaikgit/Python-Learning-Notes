
# # Getters and setters

# class Student:
    
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
        
#     def get_name(self):
#         return self.__name
    
#     def set_name(self,name):
#         self.__name = name
        
#     def set_age(self, age):
#         if isinstance(age, int):
#             self._age = age
#         else:
#             print("Age should be int. ERROR ")
            
    
# s = Student("nandan",22)

# # print(s.get_name())

# # s.set_name("divakar")

# # print(s.get_name())

# s.set_age("fgh")


#method overloading
 
# class Mathoperation:
#     def add(self,a,b):
#         print(a+b)
        
#     def add(self,a,b,c=0):
#         print(a+b+c)
        
# math = Mathoperation()
# math.add(1,2)
# math.add(1,2,3)


#method overriding

# class Animal:
    
#     def make_sound(self):
#         print("Animal is make sound")
        
# class Dog(Animal):
    
#     def make_sound(self):
#         print("Dog is barking.")
    
# d = Dog()
# d.make_sound()


# super() function

# class Animal:
    
#     def make_sound(self):
#         print("Animal is make sound")
        
# class Dog(Animal):
    
#     def make_sound(self):
#         super().make_sound()
#         print("Dog is barking.")
        
#     def get_angry(self):
#         super().make_sound()
#         self.make_sound()
        
    
# d = Dog()
# d.make_sound()
# d.make_sound()


#Abstract class

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
    
# class Bike(Vehicle):
#     def __init__(self, name):
#         self.name = name
        
#     def start_engine(self):
#         print("Starting engine")
        
        
# b = Bike("Royal Enfield")
# print(b.name)
# b.start_engine()


"""Assignement"""

# Getters and Setters:

# Create a class BankAccount with a private attribute balance.
# Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.
# Method Overloading:

# Write a class Calculator with a method multiply(). Allow it to take either two or three arguments to multiply two or three numbers.
# Method Overriding:

# Create a parent class Shape with a method draw() that prints "Drawing shape".
# Create a child class Circle that overrides draw() to print "Drawing circle".
# Abstract Classes:

# Define an abstract class Employee with an abstract method calculate_salary().
# Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.
      
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, updated_balance):
#         if updated_balance < 0:
#             print("ERROR: Balance cannot be negatve value")
#         self.__balance = updated_balance
        
# b = BankAccount(134)

# b.get_balance()
# b.set_balance(-1)


class Shape:
    def draw(self):
        print("Drawing shape")
        
class Circle(Shape):
    def draw(self):
        super().draw()
        print("Drawing circle.")
        
        
        
c = Circle()

c.draw()
         
         
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary is calculated")
            
        
