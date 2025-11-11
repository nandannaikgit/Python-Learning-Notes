"""Homework
Create a Class with a Constructor:

Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie’s title and rating.
"""
class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
        
    def display(self):
        print(f"Movie title is{self.title} and rating {self.rating}")
        
a = Movie("Kantara",5.0)
b = Movie("Kiss",4.0)

a.display()
b.display()
