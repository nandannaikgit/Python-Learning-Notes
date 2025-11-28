"""Homework
Create a Class with a Constructor:

Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie’s title and rating.
"""
# class Movie:
#     def __init__(self,title,rating):
#         self.title = title
#         self.rating = rating
        
#     def display(self):
#         print(f"Movie title is  {self.title} and rating {self.rating}")
        
# a = Movie("Kantara",5.0)
# b = Movie("Kiss",4.0)

# a.display()
# b.display()



"""
Add Default Parameters:

Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
Write a method that displays the details of each employee.
Create multiple Employee objects with different values for name and designation, and test the default salary behavior.
"""


class Employee:
    
    def __init__(self, name, designation, salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary
        
    def display(self):
        print(f"Employee name is {self.name}. Designation is {self.designation}. Salary {self.salary}")
        
E1 = Employee("nandan" , "Developer" ,50000)
E2 = Employee("pradeep" , "Tester" )
E3 = Employee("divakar" , "Manager" ,100000)
E4 = Employee("Mahantesh" , "Team Leader" ,70000)

E1.display()
E2.display()
E3.display()
E4.display()

       