from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        p3x = (p2.getX() - p1.getX()) / 2 + p1.getX()
        p3y = p2.getY() + 10
        p3 = Point(p3x, p3y)
        line1 = Line(p1, p3)
        line2 = Line(p3, p2)
        line1.draw(self.window)
        line2.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        center_x = (p2.getX() - p1.getX()) / 2 + p1.getX()
        center = Point(center_x, p1.getY())
        self.mouth = Circle(center, 10)
        self.mouth.draw(self.window)

    def wink(self):
        self.left_eye.undraw()
        p1 = self.left_eye.getCenter()
        dist = self.left_eye.getRadius()
        p2 = Point((p1.getX() + dist), p1.getY())
        p3 = Point((p1.getX() - dist), p1.getY())
        self.left_eye = Line(p2, p3)
        self.left_eye.draw(self.window)
