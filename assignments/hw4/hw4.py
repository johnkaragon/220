"""
Name: <your name goes here – first and last>
<ProgramName>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw new rectangles ")
    instructions.draw(win)

    # builds a rectangle
    shape = Rectangle(Point(50, 50), Point(75, 75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to create new rectangle
    for i in range(num_clicks):
        click = win.getMouse()
        p1 = Point(12.5 + click.getX(), 12.5 + click.getY())
        p2 = Point(-12.5 + click.getX(), -12.5 + click.getY())
        shape_1 = Rectangle(p2, p1)
        shape_1.setOutline("red")
        shape_1.setFill("red")
        shape_1.draw(win)

    clos_pt = Point(200, 50)
    c_instructions = Text(clos_pt, "Click again to close")
    c_instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("rectangles", 800, 600)
    win.setCoords(0, 0, 800, 800)
    click = win.getMouse()
    p1 = Point(click.getX(), click.getY())
    click = win.getMouse()
    p2 = Point(click.getX(), click.getY())
    rec = Rectangle(p1, p2)
    rec.setFill("light pink")
    rec.draw(win)
    x = ((p2.getX() - p1.getX()) ** 2) ** (1 / 2)
    y = ((p2.getY() - p1.getY()) ** 2) ** (1 / 2)
    area = x * y
    perimeter = (2 * x) + (2 * y)
    message = "Area: " + str(area) + "\nPerimeter: " + str(perimeter) + "\n\nClick again to close the program"
    t_area = Text(Point(400, 100), message)
    t_area.draw(win)

    win.getMouse()


def circle():
    win = GraphWin("Click to plot two points for a circle", 800, 600)
    center_p = win.getMouse()
    circum_p = win.getMouse()
    radius = ((center_p.getX() - circum_p.getX()) ** 2) + ((center_p.getY() - circum_p.getY()) ** 2)
    radius = radius ** (1/2)
    circ = Circle(center_p, radius)
    circ.setFill("red")
    circ.draw(win)
    message = "Radius: " + str(radius) + "\n\nClick again to close"
    t_message = Text(Point(400,500), message)
    t_message.draw(win)
    win.getMouse()


def pi2():
    init = 1
    pi = 4
    limit = eval(input("Enter the number of terms to sum: "))
    for i in range(1, limit):
        init += 2
        numer = 4
        for j in range(1, i + 1):
            numer *= -4
        for j in range(1, i + 1):
            numer = numer // 4
        pi += (numer / init)
    acc = ((math.pi - pi) ** 2) ** 0.5
    print("pi approximation: ", pi, "\naccuracy: ", acc)


if __name__ == '__main__':
    pass
