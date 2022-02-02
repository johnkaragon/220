from graphics import Point, GraphWin, Circle

win = GraphWin("Face", 700, 700)

face = Circle(Point(350, 175), 170)
face.draw(win)
eye1 = Circle(Point(300, 125), 45)
eye2 = eye1.clone()
eye2.move(100, 0)
eye1.setFill("Orange")
eye2.draw(win)
eye1.draw(win)

click_point = win.getMouse()
print(click_point)


#  Events - user interaction
#  - Mouse        \
#  - Key strokes --- fires an event.
#  Event Object

