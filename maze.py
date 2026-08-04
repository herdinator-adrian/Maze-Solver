from turtle import position

from cell import Cell
from window import Window
import time
import random

DRAW_SPEED = 0.001

class Maze:
    def __init__(
          self,
          x1: int,
          y1: int,
          num_rows: int,
          num_cols: int,
          cell_size_x: float,
          cell_size_y: float,
          win: Window | None = None,
          seed: int | None = None
       ) -> None:
           self.x1 = x1
           self.y1 = y1
           self.num_rows = num_rows
           self.num_cols = num_cols
           self.cell_size_x = cell_size_x
           self.cell_size_y = cell_size_y
           self.__cells = []
           self.__win = win
           if seed != None:
               random.seed(seed)

           self.__create_cells()

    def __create_cells(self):
        #self.__cells = [[Cell(self.__win) for r in range(self.num_rows)] for c in range(self.num_cols)]

        for c in range(self.num_cols):
            self.__cells.append([])
            for r in range(self.num_rows):
                self.__cells[c].append(Cell(self.__win))
                self.__draw_cell(c, r)

        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)

        entrance = self.__cells[0][0]
        print(f"Top: {entrance.has_top_wall}\n Bottom: {entrance.has_bottom_wall}\n Left: {entrance.has_left_wall}\n Right: {entrance.has_right_wall}")

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False

        if self.__win == None:
             return

        self.__draw_cell(0, 0)
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls(self, i: int, j: int):
        current_cell = self.__cells[i][j]
        current_cell.visited = True

        while True:
            possible_directions = list(filter(
                lambda x: not self.__cells[x[1][0]][x[1][1]].visited,
                self.__get_adjacent(i, j)
            ))

            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            direction = random.choice(possible_directions)

            dir, new_i, new_j = direction[0], direction[1][0], direction[1][1]
            next_cell = self.__cells[new_i][new_j]

            match dir:
                case "top":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                case "bottom":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                case "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                case "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False

            self.__draw_cell(i, j)

            self.__break_walls(new_i, new_j)


    def __get_adjacent(self, i: int, j: int) -> list[tuple[str, tuple[int, int]]]:
        # The direction by name, and the direction by indexes of column-row list.
        positions = [
            ("top", (i, j - 1)),
            ("left", (i - 1, j)),
            ("bottom", (i, j + 1)),
            ("right", (i + 1, j))
        ]

        valid = list(filter(lambda x: self.__in_maze(x[1][0], x[1][1]), positions))
        return valid

    def __in_maze(self, i: int, j: int) -> bool:
        return not (i < 0 or j < 0 or i >= self.num_cols or j >= self.num_rows)

    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False
        print("Cells visit reset.")

    def solve(self) -> bool:
        self.reset_cells_visited()
        return self.solve_r(0, 0)

    def solve_r(self, i: int, j: int) -> bool:
        self.__animate()
        current_cell = self.__cells[i][j]

        if current_cell.visited:
            raise RuntimeError(f"The cell ({i}, {j}) is visited. Did you reset the visit of the cells before running the solve algorithm?")

        current_cell.visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            print("End reached!")
            return True

        possible_directions = self.__get_adjacent(i, j)

        for direction in possible_directions:
            dir, new_i, new_j = direction[0], direction[1][0], direction[1][1]

            if not self.__in_maze(new_i, new_j):
                print(f"Cell ({new_i}, {new_j}) in {dir} is not in maze. Moving on...")
                continue

            cell = self.__cells[new_i][new_j]

            if cell.visited:
                print(f"Cell ({new_i}, {new_j}) in {dir} is visited. Moving on...")
                continue

            if ((dir == "top" and current_cell.has_top_wall)
                or (dir == "bottom" and current_cell.has_bottom_wall)
                or (dir == "left" and current_cell.has_left_wall)
                or (dir == "right" and current_cell.has_right_wall)):
                print(f"Cell ({new_i}, {new_j}) in {dir} has a wall. Moving on...")
                continue

            current_cell.draw_move(cell)
            print(f"Cell ({new_i}, {new_j}) in {dir} is valid. Moving to cell!")

            if self.solve_r(new_i, new_j):
                return True

            print(f"Cell ({new_i}, {new_j}) in {dir} is not valid. Undoing!")
            current_cell.draw_move(cell, True)

        print("No possible movements to solve found.")
        return False


    def __draw_cell(self, column: int, row: int):
        cell = self.__cells[column][row]

        x1 = self.x1 + column * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + row * self.cell_size_y
        y2 = y1 + self.cell_size_y
        cell.draw(x1, x2, y1, y2)

        self.__animate()

    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(DRAW_SPEED)
