from graphics import Point, GraphWin, Circle, Text, Entry

def convert():
    win = GraphWin("Convertor", 700, 500)
    win.setCoords(0, 0, 10, 10)
    celsius_text = Text(Point(5, 8), "Enter Celsius")
    celsius_entry = Entry(Point(5, 6), 50)
    click_text = Text(Point(5, 3), "Click to Convert")
    result_text = Text(Point(5, 1), "")

    celsius_entry.draw(win)
    celsius_text.draw(win)
    click_text.draw(win)
    result_text.draw(win)
    win.getMouse()
    celsius = eval(celsius_entry.getText())
    fahrenheit = celsius * (9 / 5) + 32
    result_text.setText(fahrenheit)
    win.getMouse()
convert()