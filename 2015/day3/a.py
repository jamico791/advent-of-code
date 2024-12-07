import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line
from utils.grids import Grid, Point
from utils.globals import Color, Direction

input_file = "data.txt"

def main():
    directions = read_first_line(input_file)
    total = 0

    grid = Grid(rows=1, cols=1, default=0, infinite=True)
    santa = Point(0, 0, color=Color.RED)
    grid.add_point(santa)
    grid.increment(santa)

    for char in directions:
        santa.shift_direction_char(char)
        grid.increment(santa)

    for block in grid.data:
        for house in block:
            if house > 0:
                total += 1

    return total

if __name__ == "__main__":
    print(main())