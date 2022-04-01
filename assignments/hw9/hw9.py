from random import randint
from graphics import GraphWin, Text, Circle, Line, Point, Entry


def get_words(file_name):
    file = open(file_name, "r")
    words_list = file.read().split("\n")
    return words_list


def get_random_word(words):
    return words[randint(1, 1000)]


def letter_in_secret_word(letter, secret_word):
    count = secret_word.count(letter)
    if count == 0:
        return False
    return True


def already_guessed(letter, guesses):
    for i in guesses:
        if letter == i:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    word = ""
    for letter in secret_word:
        found = False
        for i in range(len(guesses)):
            if letter == guesses[i]:
                word += guesses[i]
                found = True
        if not found:
            word += "_"
    return word


def won(guessed):
    for letter in guessed:
        if letter == "_":
            return False
    return True


def play_command_line(secret_word):
    print(secret_word)
    count = 0
    guessed = []
    won_ = False
    while count < 6:
        print("already guessed:", guessed)
        print("You have ", (6 - count), "guesses left")
        print(make_hidden_secret(secret_word, guessed))
        letter_guessed = input("enter a letter ")
        if not already_guessed(letter_guessed, guessed):
            if letter_in_secret_word(letter_guessed, secret_word):
                guessed.append(letter_guessed)
                guess = make_hidden_secret(secret_word, guessed)
                if won(guess):
                    print("you win")
                    won_ = True
                    count = 7
            else:
                count += 1
                guessed.append(letter_guessed)
    if not won_:
        print("word: ", secret_word)
        print("You lost, try reading a dictionary to practice! :)")


def underscore_spacer(word_):
    spaced_word = ""
    for i in word_:
        spaced_word += i + " "
    return spaced_word


def play_graphics(secret_word):
    print(secret_word)
    count = 0
    guessed = []
    won_ = False
    win = GraphWin("Hangman", 600, 600)
    win.setCoords(0, 0, 100, 100)

    gallows1 = Line(Point(10, 30), Point(30, 30))
    gallows2 = Line(Point(20, 30), Point(20, 70))
    gallows3 = Line(Point(20, 70), Point(30, 70))
    gallows4 = Line(Point(30, 70), Point(30, 60))

    gallows1.draw(win)
    gallows2.draw(win)
    gallows3.draw(win)
    gallows4.draw(win)

    person1 = Circle(Point(30, 57), 3)
    person2 = Line(Point(30, 54), Point(30, 45))
    person3 = Line(Point(30, 45), Point(35, 35))
    person4 = Line(Point(30, 45), Point(25, 35))
    person5 = Line(Point(30, 54), Point(25, 50))
    person6 = Line(Point(30, 54), Point(35, 50))
    person = [person1, person2, person3, person4, person5, person6]

    already_guessed_text = Text(Point(10, 20), guessed)
    already_guessed_text.draw(win)

    guesses_left_message = "Guesses left: " + str(6 - count)
    guesses_left_text = Text(Point(50, 30), guesses_left_message)
    guesses_left_text.draw(win)

    victory_text = Text(Point(50, 80), "You Have Won!!!!!!")

    instructions = Text(Point(50, 90), "Enter a letter and then click to submit it")
    instructions.draw(win)

    secret_word_text = Text(Point(50, 20), "")
    secret_word_text.setSize(30)
    secret_word_text.draw(win)

    entry_text = Text(Point(50, 45), "Enter your guess here: ")
    entry_text.draw(win)
    entry_ = Entry(Point(70, 45), 10)
    entry_.draw(win)

    while count < 6:
        guesses_left_message = "Guesses left: " + str(6 - count)
        guesses_left_text.setText(guesses_left_message)

        secret_word_message = underscore_spacer(make_hidden_secret(secret_word, guessed))
        secret_word_text.setText(secret_word_message)

        already_guessed_text.setText(guessed)

        win.getMouse()
        letter_guessed = entry_.getText()
        if not already_guessed(letter_guessed, guessed):
            if letter_in_secret_word(letter_guessed, secret_word):
                guessed.append(letter_guessed)
                guess = make_hidden_secret(secret_word, guessed)
                if won(guess):
                    victory_text.draw(win)
                    secret_word_message = underscore_spacer(make_hidden_secret(secret_word, guessed))
                    secret_word_text.setText(secret_word_message)
                    won_ = True
                    count = 7
            else:
                person[count].draw(win)
                count += 1
                guessed.append(letter_guessed)
    if not won_:
        message = "word: " + secret_word + "\n You lost, try reading a dictionary to practice! :)"
        victory_text.setText(message)
        victory_text.draw(win)

    win.getMouse()


if __name__ == '__main__':
    list_words = get_words("words.txt")
    word = get_random_word(list_words)
    play_graphics(word)
