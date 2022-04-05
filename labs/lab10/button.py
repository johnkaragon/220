class Button:

    def __init__(self, rectangle_shape, string_label):
        self.rectangle_s = rectangle_shape
        self.label = string_label

    def get_label(self):
        return self.label.getText()

    def set_label(self, new_label):
        self.label.setText(new_label)

    def draw(self, win):
        self.rectangle_s.draw(win)
        self.label.draw(win)

    def is_clicked(self, point):
        x = point.getX()
        y = point.getY()

        xr1 = self.rectangle_s.getP1().getX()
        yr1 = self.rectangle_s.getP1().getY()
        xr2 = self.rectangle_s.getP2().getX()
        yr2 = self.rectangle_s.getP2().getY()

        x_bool = (xr1 <= x <= xr2) or (xr2 <= x <= xr1)
        y_bool = (yr1 <= y <= yr2) or (yr2 <= x <= yr1)

        return x_bool and y_bool

    def color_button(self, color):
        self.rectangle_s.setFill(color)

    def undraw(self, win):
        self.rectangle_s.undraw(win)
        self.label.undraw(win)
