from tkinter import Tk, BOTH, Canvas
import tkinter
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.wm_title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.width = width
        self.height = height

        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(side="top", fill="x")

        self.running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

    def draw_button(self, text: str, command, x_pos: int, y_pos: int, x_size: int = 150, y_size: int = 40):
        button = tkinter.Button(self.__root, text=text, command=command)

        button.place(x=x_pos, y=y_pos, width=x_size, height=y_size)
        return button

    def draw_input(self, label_text: str, x_pos: int, y_pos: int, default_value: str = ""):
        label = tkinter.Label(self.__root, text=label_text, bg="white")
        label.place(x=x_pos, y=y_pos)

        entry = tkinter.Entry(self.__root, width=8)
        entry.insert(0, default_value)
        entry.place(x=x_pos + 80, y=y_pos)

        return entry


    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def clear_canvas(self):
        self.canvas.delete("all")


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
