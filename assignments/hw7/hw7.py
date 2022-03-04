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
    middle_man = isbn.split("-")
    num_list = []
    for i in middle_man:
        for j in i:
            num_list.append(int(j))
    counter = 0
    checker = 0
    for i in range(len(num_list), 0):
        counter += 1
        checker += counter * num_list[i]
    return checker


def send_message(file_name, friend_name):
    file1 = open(file_name, "r")
    text = file1.read()
    new_file = friend_name + ".txt"
    file2 = open(new_file, "w")
    file2.write(text)
    file1.close()
    file2.close()


def encode(message_1, key):
    encoded_m = []
    message_2 = ""
    for i in message_1:
        num = ord(i)
        encoded_m.append(num + key)
    for i in range(0, len(encoded_m)):
        message_2 += chr(encoded_m[i])
    return message_2


def send_safe_message(file_name, friend_name, key):
    file1 = open(file_name, "r")
    text = file1.read()
    text1 = " ".join(text.split("\n"))
    text2 = encode(text1, key)
    new_file = friend_name + ".txt"
    file2 = open(new_file, "w")
    file2.write(text2)
    file1.close()
    file2.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    from encryption import encode_better
    file1 = open(file_name, "r")
    text = file1.read()
    print(text)
    text1 = " ".join(text.split("\n"))
    key_file = open(pad_file_name, "r")
    key = key_file.read()
    print(key)
    text2 = encode_better(text1, key)
    new_file = friend_name + ".txt"
    file2 = open(new_file, "w")
    file2.write(text2)
    file1.close()
    key_file.close()
    file2.close()




if __name__ == '__main__':
    pass