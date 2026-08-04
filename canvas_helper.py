from window import Window

def window_align(win: Window, x_percentage_position: float, y_percentage_position: float) -> tuple[int, int]:
    return (align(win.width, x_percentage_position), align(win.height, y_percentage_position))

def align(length: int, percentage_position: float = 0.5) -> int:
    return int(length * percentage_position)
