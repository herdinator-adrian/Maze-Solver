from maze import Maze
from window import Window

def main():
    win = Window(800, 600)

    maze = Maze(
        x1=100,
        y1=100,
        num_rows=20,
        num_cols=30,
        cell_size_x=20,
        cell_size_y=20,
        win=win,
        #seed=0
    )

    maze.solve()

    win.wait_for_close()

if __name__ == '__main__':
    main()
