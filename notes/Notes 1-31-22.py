"""
Working with graphics library

Class - def: A data type
- point (x (float), y (float)) - x and y are instance variables

Classes have methods, functions specific to that class


"""
import math
from graphics import Point, GraphWin, Circle

my_point = Point(30, 20)  # takes two parameters
# my_point is a specific object, while Point() is the class type for the object
point_a = Point(70, 90)
print(point_a.getX(), point_a.getY())  # Returns a float data type

point_a.move(10, 0)
print(point_a.getX(), point_a.getY())

win = GraphWin("CSCI 220", 400, 400)
point_a.draw(win)
point_b = Point(200, 200)
point_b.draw(win)
"""
for i in range(1, 401):
    point_b.move(i, i)
    point_b.draw(win)
"""
my_circle = Circle(point_b, 100)
my_circle.draw(win)
input("hit enter to close")
# Title, Width, Height, String, Number
