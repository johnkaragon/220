"""
Name: <your name goes here – first and last>
<ProgramName>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def number_words(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    text = file.read().split()
    message = ""
    counter = 0
    for i in text:
        counter += 1
        message += str(counter) + ".) " + i + "\n"
    file.close()
    file = open(out_file_name, "w")
    file.write(message)


def hourly_wages(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    text = file.read().split()
    for i in range(2, len(text), 4):
        wage = text[i]
        wage.strip("$")
        wage2 = eval(wage) + 1.65
        text[i] = "$" + str(wage2)
    message = ""
    for i in range(0, len(text), 4):
        message += text[i] + " " + text[i + 1] + " " + text[i + 2] + "\n"
    file.close()
    file = open(out_file_name, "w")
    file.write(message)
    file.close()


def calc_check_sum(isbn):
    num_list = isbn.strip("-")


def send_message(file_name, friend_name):
    pass


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass