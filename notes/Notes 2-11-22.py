def user_name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    user_n = first[0] + last[0:7]
    print(user_n)


def month():
    months = "janfebmaraprmayjunjulaugsepoctnovdec"
    limit = eval(input("Enter a number: ")) * 3
    print("that is: ", months[limit-3: limit])


month()




