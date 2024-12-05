"""Various utilities for Advent of Code"""

def read_first_line(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        
    return line

def read_lines(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    return lines

class Grid:
    """A work in progress class to solve grid related problems"""
    def __init__(self, rows: int = 0, cols: int = 0, default: any = None, lines: list[str|list] = None):
        if rows > 0 and cols > 0:
            self.data = [[default if default != None else y + 1 for y in range(cols)] for x in range(rows)]
            self.height = rows
            self.width = cols
        elif lines:
            self.data = [[str(unit) for unit in line] for line in lines]
            self.height = len(lines)
            self.width = max(lines, key=len)
        else:
            raise ValueError("You have to specify either rows and cols, or lines")
        self.pointerx = 0
        self.pointery = 0


    def __repr__(self):
        res = ""
        i = 1
        for row in self.data:
            string_row = [str(num) for num in row]
            res += " ".join(string_row)
            if i < len(self.data):
                res += "\n"
            i += 1
        return res

    def up(self):
        """Moves the pointer up"""
        self.pointerx -= 1

    def down(self):
        """Moves the pointer down"""
        self.pointerx += 1

    def left(self):
        """Moves the pointer left"""
        self.pointery -= 1

    def right(self):
        """Moves the pointer right"""
        self.pointery += 1

    def get(self):
        return self.data[self.pointerx][self.pointery]

    def set(self, new_value):
        self.data[self.pointerx][self.pointery] = new_value

    def move_pointer(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("x and y must be integers")
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise ValueError("The pointer must lie within the boundaries of the grid.")

        self.pointerx = x
        self.pointery = y

if __name__ == "__main__":
    lines = [
        "Hello",
        "Mygoo",
        "dman."
    ]

    # grid = Grid(lines=lines)
    grid = Grid(rows=3, cols=4, default=0)

    grid.up()
    grid.right()
    grid.set(grid.get() + 1)
    grid.set(grid.get() + 1)
    grid.move_pointer(2, 3)
    grid.set(grid.get() + 1)
    # print(grid.get())


    print(grid)