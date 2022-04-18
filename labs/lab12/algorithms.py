def read_data(file_name):
    file = open(file_name, "r")
    data = []
    line = "truthy value"
    while line:
        line = file.readline()
        line_list = line.split()
        data += line_list

    file.close()
    return data


def is_in_linear(search_list, value):
    found = False
    count = 0
    while count < len(search_list):
        if search_list[count] == value:
            found = True
        count += 1
    return found


