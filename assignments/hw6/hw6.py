"""
Name: <your name goes here – first and last>
<ProgramName>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from math import *

def cash_converter():
    thing = eval(input("enter a number: "))
    text = "$ {price:.2f}"
    print(text.format(price=thing))


def encode():
    message_1 = input("Enter a message: ")
    key = eval(input("Enter a key: "))
    encoded_m = []
    message_2 = ""
    for i in message_1:
        num = ord(i)
        encoded_m.append(num + key)
    for i in range(0, len(encoded_m)):
        message_2 += chr(encoded_m[i])
    print(message_2)


def sphere_area(radius):
    area = 4 * pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4 / 3) * pi * (radius ** 3)
    return volume


def sum_n(number):
    total = 0
    for i in range(0, number):
        total += i + 1
    return total


def sum_n_cubes(number):
    total = 0
    for i in range(0, number):
        total += (i + 1) ** 3
    return total


def encode_better():
    og_message = input("Enter a message: ")
    key_message = input("Enter a message to be used as a key: ")
    message_v2 = []
    key_list = []

    for i in og_message:
        message_v2.append(ord(i) - 65)
    for i in key_message:
        key_list.append(ord(i) - 65)

    for i in range(0, len(message_v2)):
        key_num = i % len(key_list)
        message_v2[i] = (message_v2[i] + key_list[key_num]) % 58

    message_v3 = ""
    for i in range(0, len(message_v2)):
        message_v3 += chr(message_v2[i] + 65)

    print(message_v3)





if __name__ == '__main__':
    pass

