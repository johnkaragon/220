from algorithms import read_data, is_in_linear
from random import randint


def find_and_remove_first(search_list, value):
    index = search_list.index(value)
    search_list.insert(index, "John")
    search_list.pop(index + 1)


def good_input():
    good_in = False
    while not good_in:
        try:
            val = eval(input("Enter a number 1 - 10: "))
            if 1 <= val <= 10:
                good_in = True
                return val
            elif val > 10:
                print("input exceeds the upper limit of 10")
                print("Please try again")
            elif val < 1:
                print("input is less than lower limit of 1")
                print("Please try again")
        except NameError:
            print("You did not enter an number\nPlease try again")


def num_digits():
    is_positive = True
    while is_positive:
        digit = eval(input("enter a number: "))
        if digit <= 0:
            break
        count = 0
        while digit > 0:
            count += 1
            digit = digit // 10
        print("digits: ", count)


def hi_lo_game():
    target = randint(1, 100)
    won = False
    guess_count = 0
    while guess_count < 7:
        guess = eval(input("enter your guess: "))
        guess_count += 1
        if guess == target:
            print('great job, it only took you', guess_count, " guesses")
            won = True
            guess_count = 100
        elif guess < target:
            print("you guessed too low")
        else:
            print("You guessed too high")
    if not won:
        print("sorry, you lose")


def main():
    data = read_data("data_sorted.txt")
    print(data)
    print(is_in_linear(data, "10"))
    hi_lo_game()


if __name__ == "__main__":
    main()
