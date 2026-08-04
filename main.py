from maze import Maze
from window import Window
from canvas_helper import window_align

current_maze = None

def main():
    win = Window(800, 600)

    rows_input = win.draw_input("Rows:", x_pos=300, y_pos=550, default_value="15")
    cols_input = win.draw_input("Columns:", x_pos=300, y_pos=575, default_value="25")

    create_maze_button = win.draw_button(
        "Generate Maze",
        lambda: create_maze(win, rows_input, cols_input),
        100,
        550,
    )

    solve_maze_button = win.draw_button(
        "Solve Maze",
        solve_maze,
        500,
        550,
    )

    win.wait_for_close()

def create_maze(win, rows_input, cols_input):
    try:
        num_rows = int(rows_input.get())
        num_cols = int(cols_input.get())
    except ValueError:
        raise ValueError("Invalid row and column input.")

    if num_rows > 40 or num_cols > 40 or num_rows < 3 or num_cols < 3:
        raise ValueError("Values for rows and columns not allowed.")

    win.clear_canvas()

    global current_maze
    current_maze = Maze(
        x1=100,
        y1=100,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=20,
        cell_size_y=20,
        win=win,
        #seed=0
    )

def solve_maze():
    global current_maze
    if current_maze == None:
        return
    current_maze.solve()

if __name__ == '__main__':
    main()
