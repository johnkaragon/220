import math
from graphics import *
from random import randint


def bumper_car():
    width_px = 800
    height_px = 800
    win = GraphWin("click to exit", width_px, height_px)
    win.setCoords(0, 0, 400, 400)

    car_1 = Circle(Point(100, 200), 20)
    car_2 = Circle(Point(300, 200), 20)

    car_1.setFill(get_random_color())
    car_2.setFill(get_random_color())

    car_1.draw(win)
    car_2.draw(win)
    click = False

    car_1_move = [get_random(), get_random()]
    car_2_move = [get_random(), get_random()]

    while not click:
        time.sleep(0.05)

        car_1.move(car_1_move[0], car_1_move[1])
        car_2.move(car_2_move[0], car_2_move[1])

        if did_collide(car_1, car_2):
            car_2_move[0] = car_2_move[0] * -1
            car_2_move[1] = car_2_move[1] * -1
            car_1_move[0] = car_1_move[0] * -1
            car_1_move[1] = car_1_move[1] * -1

        if hit_vertical(car_1):
            car_1_move[1] = car_1_move[1] * -1

        if hit_vertical(car_2):
            car_2_move[1] = car_2_move[1] * -1

        if hit_horizontal(car_1):
            car_1_move[0] = car_1_move[0] * -1

        if hit_horizontal(car_2):
            car_2_move[0] = car_2_move[0] * -1

        mouse = win.checkMouse()

        if mouse != None:
            click = True


def did_collide(circle_one, circle_two):
    p1 = circle_one.getCenter()
    p2 = circle_two.getCenter()
    distance = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    return distance <= (circle_two.getRadius() + circle_one.getRadius())


def get_random():
    return randint(-4, 4)


def hit_vertical(car):
    center = car.getCenter().getY() + car.getRadius()
    return center >= 400 or center <= 40


def hit_horizontal(car):
    center = car.getCenter().getX() + car.getRadius()
    return center >= 400 or center <= 40


def get_random_color():
    color = color_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    return color


bumper_car()
