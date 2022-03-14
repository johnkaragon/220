def avg_calc(line):
    line_1 = line.lstrip(" ").split(" ")
    total = 0
    t_weight = 0
    print(line_1)
    for i in range(0, len(line_1), 2):
        t_weight += eval(line_1[i])
        if t_weight > 100:
            return "weight exceeds limit of 100"
        total += eval(line_1[i]) * eval(line_1[i + 1])
    if t_weight < 100:
        return "weight is less than 100"
    total = total / 100
    form = "{decimal:.1f}"
    return form.format(decimal=total)


def process(input_file, output_file):
    reading = open(input_file, "r")
    text = reading.read().split("\n")
    new_text = ""
    for i in range(0, len(text)):
        line = text[i].split(":")
        new_line = line[0] + "'s average: " + avg_calc(line[1]) + "\n"
        new_text += new_line
    reading.close()
    writing = open(output_file, "w")
    print(new_text, file=writing)
    writing.close()


def main():
    if __name__ == "__main__":
        process("grades.txt", "avg.txt")


main()
