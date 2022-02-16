from graphics import *

win = GraphWin("Valentines", 700, 700)
win.setCoords(0, 0, 700, 700)
text = Text(Point(350, 600), "click to begin")
text_2 = Text(Point(350, 100), "click again to close")
rec = Polygon(Point(350, 150), Point(450, 250), Point(350, 350), Point(250, 250))
rec.setFill("pink")
rec.setOutline("pink")
circ_1 = Circle(Point(400, 300), 72)
circ_2 = Circle(Point(300, 300), 72)
circ_2.setFill("pink")
circ_1.setFill("pink")
circ_1.setOutline("pink")
circ_2.setOutline("pink")
line = Line(Point(50, 350), Point(150, 350))
line.setArrow("last")


text.draw(win)
win.getMouse()
line.draw(win)
text.setText("Happy Valentines Day")
rec.draw(win)
circ_1.draw(win)
circ_2.draw(win)
for i in range(30):
    line.move(10, 0)
    time.sleep(0.1)
line.undraw()
line.move(30,0)
line.draw(win)
text_2.draw(win)
for i in range(30):
    line.move(10, 0)
    time.sleep(0.1)

win.getMouse()

