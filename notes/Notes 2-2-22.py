from graphics import Point, GraphWin, Circle, Text, Entry

win = GraphWin("Face", 700, 700)
win.setCoords(00, 00, 700, 700)

face = Circle(Point(350, 175), 170)
face.draw(win)
eye1 = Circle(Point(300, 125), 45)
eye2 = eye1.clone()
eye2.move(100, 0)
eye1.setFill("Orange")
name = Text(Point(350, 600), "James")

pointer = Point(350, 500)

pointer.draw(win)
eye2.draw(win)
eye1.draw(win)
name.draw(win)

user_input = Entry(Point(350, 350), 50)
user_input.setText("Enter your name ")
user_input.draw(win)
win.getMouse()
name = user_input.getText()
print(name)

click_point = win.getMouse()
print(click_point)

#  Events - user interaction
#  - Mouse        \
#  - Key strokes --- fires an event.
#  Event Object
