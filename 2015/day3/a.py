import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line
from utils.grids import Grid
from utils.globals import Color

input_file = "data.txt"

def main():
    directions = read_first_line(input_file)
    total = 0

    grid = Grid(rows=1, cols=1, default=0, infinite=True)
    pointer_name = "santa"
    grid.add_pointer(pointer_name, Color.red.value)
    grid.set_pointer_value(pointer_name, grid.get_pointer_value(pointer_name) + 1)

    for char in directions:
        if char == "^":
            grid.north(pointer_name)
        elif char == "v":
            grid.south(pointer_name)
        elif char == ">":
            grid.east(pointer_name)
        elif char == "<":
            grid.west(pointer_name)
        grid.set_pointer_value(pointer_name, grid.get_pointer_value(pointer_name) + 1)

    for block in grid.data:
        for house in block:
            if house > 0:
                total += 1

    return total

if __name__ == "__main__":
    print(main())