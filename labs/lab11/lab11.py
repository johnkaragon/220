from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint


def main():
    win = GraphWin("", 650, 650)
    win.setCoords(0, 0, 100, 100)
    acc = 0
    acc2 = 0

    b_rec = Rectangle(Point(40, 10), Point(60, 30))
    b_text = Text(Point(50, 20), "")

    b = Button(b_rec, b_text)
    b.set_label("exit")
    b.draw(win)

    score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
    score = Text(Point(50, 90), score_message)
    score.draw(win)

    play_again = Text(Point(50, 40), "Click to play again.")

    while True:
        door_list = []
        x1 = -10
        x2 = 10
        y1 = 50
        y2 = 80
        for i in range(1, 4):
            p1 = Point((x1 + (25 * i)), y1)
            p2 = Point((x2 + (25 * i)), y2)
            message = "door " + str(i)
            t_point_x = (x1 + 10) + (25 * i)
            t_point = Point(t_point_x, 65)

            d = Door(Rectangle(p1, p2), Text(t_point, message))
            door_list.append(d)

        for door in door_list:
            door.draw(win)

        secret = randint(0, 2)
        door_list[secret].set_secret(True)

        d1 = door_list[0]
        d2 = door_list[1]
        d3 = door_list[2]

        point = win.getMouse()
        if b.is_clicked(point):
            break

        elif d1.is_clicked(point):
            is_secret = d1.is_secret()
            if is_secret:
                d1.close("green", "Correct!")
                acc += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                win.getMouse()
                play_again.undraw()
            else:
                d1.open("red", "incorrect...")
                acc2 += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                point = win.getMouse()
                if b.is_clicked(point):
                    break
                play_again.undraw()

        elif d2.is_clicked(point):
            is_secret = d2.is_secret()
            if is_secret:
                d2.close("green", "Correct!")
                acc += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                win.getMouse()
                play_again.undraw()
            else:
                d2.open("red", "incorrect...")
                acc2 += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                point = win.getMouse()
                if b.is_clicked(point):
                    break
                play_again.undraw()

        elif d3.is_clicked(point):
            is_secret = d3.is_secret()
            if is_secret:
                d3.close("green", "Correct!")
                acc += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                win.getMouse()
                play_again.undraw()
            else:
                d3.open("red", "incorrect...")
                acc2 += 1
                score_message = "score-\nwins: " + str(acc) + "\nlosses: " + str(acc2)
                score.setText(score_message)
                play_again.draw(win)
                point = win.getMouse()
                if b.is_clicked(point):
                    break
                play_again.undraw()

        d1.undraw(win)
        d2.undraw(win)
        d3.undraw(win)


main()
