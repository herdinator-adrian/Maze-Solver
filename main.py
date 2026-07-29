from point import Point, Line
from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    win.wait_for_close()

    point1 = Point(200, 300)
    point2 = Point(400, 500)

    line = Line(point1, point2)

    line.draw(win.canvas)

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(side="top", fill="x")

        self.running = False
        pass

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

if __name__ == '__main__':
    main()
