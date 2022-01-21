"""
Name: <John Aragon>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)



def calc_volume():
   length = eval(input("Enter the length: "))
   width = eval(input("Enter the width: "))
   height = eval(input("Enter the height: "))
   vol = length * width * height
   print("Volume = ", vol)


def shooting_percentage():
    total = eval(input("How many total shots did the player take? "))
    shots_made = eval(input("How many of those shots were successful? "))
    percent = (shots_made/total) * 100
    print("Shooting percentage: ", percent)


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    cost = ((10.50 + 0.86) * pounds) + 1.50
    print("Your total is ", cost)
    #Coffee


def kilometers_to_miles():
    kilos = eval(input("how many kilometers did you travel? "))
    miles = kilos / 1.61
    print("Thats ", miles, " miles!")


if __name__ == '__main__':
    pass