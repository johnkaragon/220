from graphics import GraphWin, Entry, Text, Rectangle, Point
from math import *

win = GraphWin("Vignonne", 600, 600)
win.setCoords(0, 0, 100, 100)

text_1 = Text(Point(50, 80), "Enter a message to be coded: ")
text_1.draw(win)

message_e = Entry(Point(50, 75), 30)
message_e.draw(win)

key_e = Entry(Point(50, 55), 20)
key_e.draw(win)

text_2 = Text(Point(50, 60), "Enter a key: ")
text_2.draw(win)

button = Rectangle(Point(40, 20), Point(60, 30))
button.draw(win)

text_3 = Text(Point(50, 25), "Encode")
text_3.draw(win)

win.getMouse()  # before typing

button.undraw()
text_3.undraw()

message = message_e.getText()
message = message.upper()
message2 = message.split(" ")
message = "".join(message2)

key = key_e.getText()
key = key.upper()
key2 = key.split(" ")
key = "".join(key2)

proto_message = []
for i in message:
    proto_message.append(ord(i) - 65)

real_key = []
for j in key:
    real_key.append(ord(j) - 65)

encoded_message = []
for k in range(0, len(proto_message)):
    key_num = k % len(real_key)
    instance = (proto_message[k] + real_key[key_num]) % 26
    encoded_message.append(chr(instance + 65))

encoded = "".join(encoded_message)
text_4 = Text(Point(50, 25), encoded)
text_4.draw(win)

text_5 = Text(Point(50, 15), "Click again to close")
text_5.draw(win)

win.getMouse()
win.close()
