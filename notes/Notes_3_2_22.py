"""
We can test multiple conditions at one with "and"

bool and bool

and truth table:
    p   |   q   |   p and q
    T       F       F
    F       T       F
    F       F       F
    T       T       T

"""


def max_(a, b, c):
    if a >= b and a >= c:
        return a  # return statement end the execution of a function
    elif b >= a and b >= c:
        return b
    else:
        return c


def max_2(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    elif b >= c:
        return b
    return c


def max_3(a, b, c):
    max_val = a
    if max_val <= b:
        max_val = b
    if max_val <= c:
        max_val = c
    return max_val

