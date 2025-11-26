
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

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Bike(Vehicle):
    def __init__(self, name):
        self.name = name
        
    def start_engine(self):
        print("Starting engine")
        
        
b = Bike("Royal Enfield")
print(b.name)
b.start_engine()


"""Assignement"""
        
