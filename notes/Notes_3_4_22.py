"""

for loops: definite loop
    - Knows where it'll start and end

indefinite loops:
    - Knows where they'll star, but not when they'll stop

while <condition> :
    <body>


"""
from graphics import *


def my_first_while():
    for i in range(5):
        print(i)

    counter = 0
    while counter != 5:
        print(counter)
        counter += 1


def is_equal(p1, p2):
    return p1.getX() == p2.getX() and p1.getY() == p2.getY()


def is_game_over(p1_points, p2_points):
    if p1_points >= 15 or p2_points >= 15:
        return True
    return False


player1 = 9
player2 = 15
while not is_game_over(player1, player2):
    one, two = eval(input("enter xcore for player one and two"))
    player1 += one
    player2 += two

