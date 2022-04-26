from lab12.algorithms import is_in_binary, selection_sort, area_calc, rect_sort
from graphics import Point, Rectangle


def main():
    t_list = [0, 3, 4, 5, 6, 9, 10, 11, 14, 15, 16, 17, 20, 23, 27, 28]
    print(is_in_binary(29, t_list))

    sort_list = [10, 48, 1, 98, 12, 64, 12, 13, 45, 48]
    print(selection_sort(sort_list))
    print()
    print()

    rectangles = [Rectangle(Point(0, 0), Point(90, 59)),
                  Rectangle(Point(0, 0), Point(60, 54)),
                  Rectangle(Point(0, 0), Point(97, 64)),
                  Rectangle(Point(0, 0), Point(77, 94)),
                  Rectangle(Point(0, 0), Point(47, 38)),
                  Rectangle(Point(0, 0), Point(29, 800))]
    count = 0
    for i in rectangles:
        count += 1
        print(area_calc(i), " : ", count)

    print(rect_sort(rectangles))

    count = 0
    for i in rectangles:
        count += 1
        print(area_calc(i), " : ", count)

    info = signal_find("signals.txt")
    print("number of good signals: ", info[0],
          "\nsignals in range: ", info[1],
          "\nnumber of signals searched: ", info[2])


def signal_find(filename):
    signals_list = open(filename, "r").read().split()
    good_signals = 0
    good_signals_list = []
    searched = 0

    for i in range(len(signals_list)):
        if 4000 < int(signals_list[i]) < 5000:
            good_signals += 1
            good_signals_list.append(signals_list[i])
            if good_signals == 5:
                searched = i + 1
                break

    return [good_signals, good_signals_list, searched]


if __name__ == "__main__":
    main()
