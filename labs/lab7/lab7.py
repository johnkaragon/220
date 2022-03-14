def avg_calc(line):
    line_1 = line.lstrip(" ").split(" ")
    total = 0
    t_weight = 0
    for i in range(0, len(line_1), 2):
        t_weight += eval(line_1[i])
        if t_weight > 100:
            return "weight exceeds limit of 100"
        total += eval(line_1[i]) * eval(line_1[i + 1])
    if t_weight < 100:
        return "weight is less than 100"
    total = total / 100
    form = "{decimal:.1f}"
    return eval(form.format(decimal=total))


def weighted_average(input_file, output_file):
    reading = open(input_file, "r")
    text = reading.read().split("\n")
    new_text = ""
    class_total = 0
    class_counter = 0
    for i in range(0, len(text)):
        read_line = text[i].split(":")
        avg = avg_calc(read_line[1])
        if type(avg) == float:
            class_total += avg
            class_counter += 1
        new_line = read_line[0] + "'s average: " + str(avg) + "\n"
        new_text += new_line
    reading.close()
    class_total = class_total / class_counter
    form = "{decimal:.1f}"
    nclass_total = form.format(decimal=class_total)
    new_text += "class average: " + str(nclass_total)
    writing = open(output_file, "w")
    print(new_text, file=writing)
    writing.close()


def main():
    if __name__ == "__main__":
        weighted_average("grades.txt", "avg.txt")


main()
