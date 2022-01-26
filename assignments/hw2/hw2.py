"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    limit = eval(input("Enter the upper limit of the calculation: "))
    total = 0
    for i in range(1, limit + 1):
        if i % 3 == 0:
            total += i
    print(total)


def multiplication_table():
    for i in range(1, 11):
        line = ""
        for j in range(1, 11):
            if j == 10:
                line = line + str(i * j)
                print(line)
            else:
                line = line + (str(i * j) + "\t")


def triangle_area():
    a_side = eval(input("Enter the length of side a: "))
    b_side = eval(input("Enter the length of side b: "))
    c_side = eval(input("Enter the length of side c: "))
    s_var = (a_side + b_side + c_side) / 2
    area = math.sqrt(s_var * (s_var - a_side) * (s_var - b_side) * (s_var - c_side))
    print("area: ", area)


def sum_squares():
    low_lim = eval(input("Enter the lower limit of the function: "))
    high_lim = eval(input("Enter the upper limit of the function: "))
    total = 0
    for i in range(low_lim, high_lim + 1):
        total += i ** 2
    print(total)


def power():
    base = eval(input("Enter the base: "))
    exp = eval(input("Enter the power: "))
    ans = base
    for i in range(1, exp):
        ans = ans * base
    print(ans)


if __name__ == '__main__':
    pass
