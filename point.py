class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Line:
    DEFAULT_FILL_COLOR ="black"

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_middle_point(self) -> Point:
        return Point((self.point1.x + self.point2.x) / 2, (self.point1.y + self.point2.y) / 2)

    def draw(self, canvas, fill_color = DEFAULT_FILL_COLOR):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill= fill_color,
            width = 2
        )
