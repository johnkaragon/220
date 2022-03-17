"""
Name: John Aragon
<ProgramName>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    num = []
    for i in range(len(nums)):
        num.append(nums[i] * nums[i])
    return num


def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum


def to_numbers(nums):
    real_num = []
    for i in range(len(nums)):
        real_num.append(eval(nums[i]))
    return real_num


def sum_of_squares(nums):
    list2 = []
    for i in range(len(nums)):
        list_p = nums[i].split(",")
        list1 = to_numbers(list_p)
        list2.append(sum_list(square_each(list1)))
    return list2


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    by_four = year % 4 == 0
    by_100 = year % 100 == 0
    by_400 = year % 400 == 0
    print((not by_100 or by_400) and by_four)


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light blue")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        text = Text(Point(5, 1), "The circles overlap")
        text.draw(win)
    else:
        text = Text(Point(5, 1), "The circles do not overlap")
        text.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    p1 = circle_one.getCenter()
    p2 = circle_two.getCenter()
    distance = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    return distance <= (circle_two.getRadius() + circle_one.getRadius())


if __name__ == '__main__':
    print(starter(150, 1))