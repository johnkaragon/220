class Door:

    def __init__(self, shape, text):
        self.shape = shape
        self.text = text
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, new_text):
        self.text.setText(new_text)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self, win):
        self.shape.undraw(win)
        self.text.undraw(win)

    def is_clicked(self, point):
        x = point.getX()
        y = point.getY()

        xr1 = self.shape.getP1().getX()
        yr1 = self.shape.getP1().getY()
        xr2 = self.shape.getP2().getX()
        yr2 = self.shape.getP2().getY()

        x_bool = (xr1 <= x <= xr2) or (xr2 <= x <= xr1)
        y_bool = (yr1 <= y <= yr2) or (yr2 <= x <= yr1)

        return x_bool and y_bool

    def color_door(self, color):
        self.shape.setFill(color)

    def open(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def close(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def is_secret(self):
        return self.secret

    def set_secret(self, val):
        self.secret = val
