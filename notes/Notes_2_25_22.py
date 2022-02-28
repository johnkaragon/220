"""
Control structures alter the flow of the code
example: functions, loops, etc...

Decision Structures -
 - Allows program to execute different statements depending on some condition

bool - data type
 - can either be "true" or "false"
"""


def convert():
    celsius = eval(input("Enter temp: "))
    fahrenheit = celsius * (9 / 5) + 32
    print("the temp is ", fahrenheit)
    if fahrenheit > 90:
        print("whoa that's hot")
    if fahrenheit < 30:
        print("brrr that's cold")

print(__name__)
