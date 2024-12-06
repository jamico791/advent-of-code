"""Various utilities for Advent of Code"""

from enum import Enum

def read_first_line(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        
    return line

def read_lines(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    return lines

class Color(Enum):
    default = "\033[0m"
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"

class Pointer:
    def __init__(self, x: int, y: int, name: str, color: str):
        self.x = x
        self.y = y
        self.name = name
        self.color = color

class Grid:
    """A work in progress class to solve grid related problems"""
    def __init__(self, rows: int = 0, cols: int = 0, default: any = None, lines: list[str|list] = None, infinite: bool = False):
        if rows > 0 and cols > 0:
            self.data = [[default if default != None else y + 1 for y in range(cols)] for x in range(rows)]
            self.height = rows
            self.width = cols
        elif lines:
            self.data = [[str(unit) for unit in line] for line in lines]
            self.height = len(self.data)
            self.width = len(self.data[0])
        else:
            raise ValueError("You have to specify either rows and cols, or lines")
        self.default = default
        self.infinite = infinite
        self.pointers: dict[str:Pointer] = {}

    def __repr__(self):
        res = ""
        i = 1
        for row in self.data:
            j = 1
            for char in row:
                pointer = None
                for p in self.pointers.values():
                    if p.x == j and p.y == i:
                        pointer = p
                if j > 1:
                    res += " "
                if pointer:
                    res += pointer.color
                res += str(char)
                if pointer:
                    res += Color.default.value
                if i < len(self.data) and j ==len(row):
                    res += "\n"
                j += 1
            i += 1
        return res

    def add_pointer(self, name: str, color: str):
        pointer = Pointer(1, 1, name, color)
        self.pointers[name] = pointer

    def north(self, name):
        """Moves the pointer up"""
        pointer = self.get_pointer(name)
        self.move_pointer(name, pointer.x, pointer.y - 1)

    def east(self, name: str):
        """Moves the pointer right"""
        pointer = self.get_pointer(name)
        self.move_pointer(name, pointer.x + 1, pointer.y)

    def south(self, name: str):
        """Moves the pointer down"""
        pointer = self.get_pointer(name)
        self.move_pointer(name, pointer.x, pointer.y + 1)

    def west(self, name: str):
        """Moves the pointer left"""
        pointer = self.get_pointer(name)
        self.move_pointer(name, pointer.x - 1, pointer.y)
    
    def northeast(self, name: str):
        self.north(name)
        self.east(name)

    def northwest(self, name: str):
        self.north(name)
        self.west(name)

    def southwest(self, name: str):
        self.south(name)
        self.west(name)

    def southeast(self, name: str):
        self.south(name)
        self.east(name)

    def get_pointer_value(self, pointer_name: str):
        pointer = self.get_pointer(pointer_name)
        return self.data[pointer.y - 1][pointer.x - 1]

    def set_pointer_value(self, pointer_name: str, new_value: any):
        pointer = self.get_pointer(pointer_name)
        self.data[pointer.y - 1][pointer.x - 1] = new_value
    
    def get_pointer(self, name: str):
        return self.pointers[name]

    def move_pointer(self, name: str, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("x and y must be integers")
        pointer = self.get_pointer(name)
        pointer.x = x
        pointer.y = y

        if self.infinite:
            if x < 1:
                for row in self.data:
                    for _ in range(1 - x):
                        row.insert(0, self.default)
                    pointer.x = 1
                self.width = len(max(self.data, key=len))
            elif x > self.width:
                for row in self.data:
                    for _ in range(x - self.width):
                        row.append(self.default)
                self.width = len(max(self.data, key=len))
            if y < 1:
                for _ in range(1 - y):
                    self.data.insert(0, [self.default for n in range(self.width)])
                pointer.y = 1
                self.height = len(self.data)
            if y > self.height:
                for _ in range(y - self.height):
                    self.data.append([self.default for n in range(self.width)])
                self.height = len(self.data)
        elif x < 1 or y < 1 or x > self.width or y > self.height:
            raise ValueError("The pointer must lie within the boundaries of the grid.")

if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            print(i, j)