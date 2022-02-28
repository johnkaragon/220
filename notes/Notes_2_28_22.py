import math


def quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print("No real roots")
    # if disc >= 0:
    else:
        if disc == 0:
            sqrt_discr = math.sqrt()
            denom = 2 * a
            root_1 = (-b + sqrt_discr) / denom
            print(root_1)
        else:
            sqrt_discr = math.sqrt()
            denom = 2 * a
            root_1 = (-b + sqrt_discr) / denom
            root_2 = (-b - sqrt_discr) / denom
            print(root_1, ", ", root_2)
