from graphics import GraphWin, Rectangle, Text, Point
from button import Button
from door import Door



def main():
    win = GraphWin("", 650, 650)
    win.setCoords(0, 0, 100, 100)

    b_rec = Rectangle(Point(40, 70), Point(60, 90))
    b_text = Text(Point(50, 80), "")

    b = Button(b_rec, b_text)
    b.set_label("exit")
    b.draw(win)

    d_rec = Rectangle(Point(40, 20), Point(60, 60))
    d_text = Text(Point(50, 40), "")

    d = Door(d_rec, d_text)
    d.open("white", "open")
    d.draw(win)

    while True:
        point = win.getMouse()
        if b.is_clicked(point):
            break

        elif d.is_clicked(point):
            if d.get_label() == "open":
                d.close("red", "closed")
            else:
                d.open("white", "open")





if __name__ == "__main__":
    main()