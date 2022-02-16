"""
Name: <your name goes here – first and last>
<ProgramName>.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    names = input("enter your name (first and then last): ")
    sep_names = names.split(" ")
    print(sep_names[1], " ", sep_names[0])


def company_name():
    domain = input("enter the domain: ")
    parts = domain.split(".")
    print(parts[1])


def initials():
    limit = eval(input("Enter how many students are in the class: "))
    for i in range(0, limit):
        message = "Enter the name of student " + str(i + 1) + ": "
        name = input(message)
        splitter = name.split(" ")
        initial = ""
        for j in range(2):
            stand_in = splitter[j]
            initial = initial + stand_in[0]
        print(initial)


def names():
    names_list = input("enter a list of names: ")
    initials_list = ""
    separated = names_list.split(",")
    for i in range(len(separated)):
        name = separated[i]
        name = name.lstrip()
        splitter = name.split(" ")
        initial = ""
        for j in range(2):
            stand_in = splitter[j]
            initial = initial + stand_in[0]
        initials_list = initials_list + initial + " "
    print(initials_list)


def thirds():
    limit = eval(input("How many sentences? "))
    total = ""
    for i in range(limit):
        message = "Enter sentence " + str(i + 1) + ": "
        sentence = input(message)
        total += sentence + ";"
    total_l = total.split(";")
    for i in range(len(total_l)):
        third = ""
        line = total_l[i]
        for j in range(0, len(line), 3):
            third += line[j]
        print(third)


def word_average():
    sentence = input("Enter a sentence: ")
    total = 0
    words = sentence.split(" ")
    for i in range(len(words)):
        word = words[i]
        total += len(word)
    print(total / len(words))


def pig_latin():
    sentence = input("Enter a sentence: ")
    pig_sentence = ""
    words = sentence.split(" ")
    for i in range(len(words)):
        word = words[i]
        pig_word = word[1:len(word)] + word[0] + "ay"
        pig_sentence += pig_word + " "
    print(pig_sentence)


pig_latin()
if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass