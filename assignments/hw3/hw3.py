"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    limit = eval(input("How many grades will you enter? "))
    total = 0
    for i in range(0,limit):
        grade = eval(input("Enter Grade: "))
        total = total + grade
    print("Average: ", (total / limit))


def tip_jar():
    total_tips = 0
    for i in range(0, 5):
        total_tips = total_tips + eval(input("How much will you tip? "))
    print("The total amount of tips is ", total_tips)


def newton():
    base = eval(input("What number would you like to find the square root of? "))
    init = base
    improve = eval(input("How many times should we improve the approximation? "))
    for i in range(0, improve):
        base = (base + (init / base)) / 2
    print(base)


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
