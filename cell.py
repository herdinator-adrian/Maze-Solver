from point import Point, Line
from window import Window
class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = window

    def draw(self, x1: float, x2: float, y1: float, y2: float):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win == None:
            return

        self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black" if self.has_left_wall else "white")
        self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black" if self.has_bottom_wall else "white")
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black" if self.has_top_wall else "white")
        self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black" if self.has_right_wall else "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if self.__win == None:
            return

        fill_color = "red"
        if undo:
            fill_color = "gray"
        point1 = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        point2 = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)

        self.__win.draw_line(Line(point1, point2), fill_color)
