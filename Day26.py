# class Notification:
#     def send(self):
#         print("Notification sent")

# class EmailNotification(Notification):
#     def send(self):
#         print("Email sent.")
        
# class SMSNotification(Notification):
#     def send(self):
#         print("SMS sent")
        

# """
# Inheritance:

# Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() method.
# Demonstrate how the Bike can use both start and ride.

# """

# class Vehicle:
#     def start(self):
#         print("Vehicle starting")
        
# class Bike(Vehicle):
#     def __init__(self,name):
#         self.name = name
        
#     def ride(self):
#         print("Bike is riding.")
        
# b = Bike("Royal Enfield")

# b.start()
# b.ride()
        
        
        
        
"""Polymorphism:

Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. Each class should calculate area differently based on its shape.
Create a loop to calculate areas for both Circle and Rectangle objects.
"""

class Shape:
    def cal_area(self):
        print("Calculated area.")
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def cal_area(self):
        print(f"Area of circle: {(22/7)*self.radius*self.radius}")
        
        
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
        
    def cal_area(self):
        print(f"Area of rectangle: {self.l*self.b}")
 
c = Circle(5)
r = Rectangle(3,2)

c.cal_area()
r.cal_area()

       