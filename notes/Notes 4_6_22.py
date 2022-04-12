from graphics import Point, Circle


"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [10, 11, 12]

abc = a + b + c
print(abc)

cab = c + b + a
print("\n\n", cab)
cab.sort()  # Can also sort by strings (alphabetically)
print(cab)

bca = b + c + a
print("\n\n", bca)
bca.reverse()
print(bca)
bca.sort(reverse=True)  # Can also sort by strings (alphabetically)
print(bca)
print(bca.index(10))
bca.insert(2, 90)  # Adds the value 90 to position 2, moves the former value at position 2 to position 3
print(bca)

"""


def x_sort(circle):
    return circle.getCenter().getX()


def y_sort(circle):
    return circle.getCenter().getY()

def radius_sort(circle):
    return circle.getRadius()

def print_c(circles):
    for circle in circles:
        print("({}, {}) {} ".format(circle.getCenter().getX(),
                                    circle.getCenter().getY(),
                                    circle.getRadius()))


def main():
    c1 = Circle(Point(2, 3), 90)
    c2 = Circle(Point(45, 3), 9)
    c3 = Circle(Point(20, 67), 990)
    c4 = Circle(Point(4, 12), 909)
    c5 = Circle(Point(98, 7), 78)
    c6 = Circle(Point(23, 91), 65)
    circles = [c1, c2, c3, c4, c5, c6]

    print_c(circles)
    print("\nby x-value:")

    circles.sort(key=x_sort)
    print_c(circles)
    print("\nby y-value:")

    circles.sort(key=y_sort)
    print_c(circles)
    print("\nby radius:")

    circles.sort(key=radius_sort)
    print_c(circles)


"""
list = [_, _, _, _]
tuple = (_, _, _, _)
dictionary = {_, _, _, _}

tuples and lists are very similar, most of the functions you could do on a list, you can do on a tuple
- tuples do not allow you to change an item within the tuple

math.pi.pi.pi..pi.pi.pi.pi
"""


if __name__ == '__main__':
    main()
