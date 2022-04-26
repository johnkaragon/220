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


def is_in_binary(target, search_list):
    left_bound = 0
    right_bound = len(search_list) - 1
    found = False
    while not found:
        middle_value = (left_bound + right_bound) // 2
        if search_list[middle_value] == target:
            found = True
            return found
        elif search_list[middle_value] < target:
            left_bound = middle_value + 1
        elif search_list[middle_value] > target:
            right_bound = middle_value - 1
        if right_bound < left_bound:
            return found


def selection_sort(to_sort):
    for i in range(len(to_sort)):
        for j in range(i, len(to_sort)):
            if to_sort[j] < to_sort[i]:
                current_val = to_sort[i]
                smaller_val = to_sort[j]
                to_sort[i] = smaller_val
                to_sort[j] = current_val

    return to_sort


def rect_sort(rec_list):
    for i in range(len(rec_list)):
        for j in range(i, len(rec_list)):
            if area_calc(rec_list[j]) < area_calc(rec_list[i]):
                current_val = rec_list[i]
                smaller_val = rec_list[j]
                rec_list[i] = smaller_val
                rec_list[j] = current_val


def area_calc(rec):
    x = ((rec.getP1().getX() - rec.getP2().getX()) ** 2) ** (1 / 2)
    y = ((rec.getP1().getY() - rec.getP2().getY()) ** 2) ** (1 / 2)
    return x * y
