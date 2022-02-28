from graphics import Point
from math import *


def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    square = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return square


def sum_diff(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val, diff_val


def get_discount(price, sale):
    price = price - (price * sale)
    return price


def change_point(p, x, y):
    p.move(x, y)


def double_list(list_one):
    for index in range(len(list_one)):
        list_one[index] = list_one[index] * 2


my_list = [1, 2, 5, 9, 100, 23.3]


print(double_list(my_list))
print(my_list)

print(sum_diff(3, 10))
print(distance(Point(3, 40), Point(30, 7)))
print(get_discount(23.40, .15))
