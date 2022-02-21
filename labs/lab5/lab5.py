from graphics import *
from math import *


def triangle():
    win = GraphWin("Clicks", 600, 600)

    a = win.getMouse()
    b = win.getMouse()
    c = win.getMouse()

    tri = Polygon(a, b, c)
    tri.draw(win)

    ab = sqrt(((a.getX() - b.getX()) ** 2) + (( a.getY() - b.getY()) ** 2))
    bc = sqrt(((b.getX() - c.getX()) ** 2) + (( b.getY() - c.getY()) ** 2))
    ca = sqrt(((c.getX() - a.getX()) ** 2) + (( c.getY() - a.getY()) ** 2))

    perimeter = ab + bc + ca
    s = (ab + bc + ca) / 2
    area = sqrt(s * (s - ab) * (s - bc) + (s- ca))

    message = "Area: " + str(area) +"\nPerimeter: " + str(perimeter)
    text = Text(Point(300, 500), message)
    text.draw(win)

    win.getMouse()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    blue_entry_pt = blue_text_pt.clone()
    green_entry_pt = green_text_pt.clone()
    red_entry_pt = red_text_pt.clone()
    blue_entry_pt.move(60, 0)
    green_entry_pt.move(60, 0)
    red_entry_pt.move(60, 0)

    blue_entry = Entry(blue_entry_pt, 5)
    green_entry = Entry(green_entry_pt, 5)
    red_entry = Entry(red_entry_pt, 5)



    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)
    green_entry.draw(win)
    red_entry.draw(win)

    for i in range(0, 5):
        win.getMouse()
        red = eval(red_entry.getText())
        blue = eval(blue_entry.getText())
        green = eval(green_entry.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    win.getMouse()
    win.close()


def process_string():
    thing = input("Enter whatever you'd like to:")
    print(thing[0])
    print(thing[-1])
    print(thing[1:5])
    print(thing[0] + thing[-1])
    print(thing[0:3] * 10)
    for i in thing:
        print(i)
    print(len(thing))


def process_list():
    pt = Point(5, 10)
    values = [5,  "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = eval(values[2]) + eval(values[0])
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[0], values[3], values[4]]
    print(x)
    x = values[0] + values[2] + eval(values[-1])
    print(x)
    x = len(values)
    print(x)


def another_series():
    values = [2, 4, 6]
    limit = eval(input("enter how many terms: "))
    total = 0
    total_2 = ""
    for i in range(0, limit):
        total += values[i % 3]
        total_2 = total_2 + str(values[i % 3]) + " "
    print(total_2, "\ntotal: ", total)


def target():
    win = GraphWin("", 650, 650)
    win.setCoords(0, 0, 100, 100)
    center = Point(50, 50)
    yCirc = Circle(center, 10)
    rCirc = Circle(center, 10 * 2)
    bluCirc = Circle(center, 10 * 3)
    blaCirc = Circle(center, 10 * 4)
    wCirc = Circle(center, 10 * 5)

    wCirc.setFill("white")
    blaCirc.setFill("black")
    bluCirc.setFill("blue")
    rCirc.setFill("red")
    yCirc.setFill("yellow")

    wCirc.draw(win)
    blaCirc.draw(win)
    bluCirc.draw(win)
    rCirc.draw(win)
    yCirc.draw(win)
    win.getMouse()

