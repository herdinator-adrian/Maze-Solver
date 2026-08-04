from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.wm_title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(side="top", fill="x")

        self.running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
