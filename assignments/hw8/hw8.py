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


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]


def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]


def to_numbers(nums):
    real_num = []
    for i in range(len(nums)):
        real_num.append(eval(nums[i]))


def sum_of_squares(nums):
    pass


def starter(weight, wins):
    if 150 <= weight < 160 and wins > 5:
        return True
    elif weight >= 199 or wins > 20:
        return True
    return False


def leap_year(year):
    pass


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

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass


if __name__ == '__main__':
    pass