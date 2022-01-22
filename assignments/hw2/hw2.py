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
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("area: ", area)


def sum_squares():
    lowlim = eval(input("Enter the lower limit of the function: "))
    highlim = eval(input("Enter the upper limit of the function: "))
    total = 0
    for i in range(lowlim,highlim +1):
        total += i ** 2
    print(total)


def power():
    pass


if __name__ == '__main__':
    pass
