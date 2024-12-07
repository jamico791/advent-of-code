import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line
from utils.grids import Grid, Point
from utils.globals import Color, Direction

input_file = "example.txt"

def main():
    directions = read_first_line(input_file)
    total = 0

    grid = Grid(rows=1, cols=1, default=0, infinite=True)
    santa = Point(0, 0, Color.RED)
    robo_santa = Point(0, 0, Color.GREEN)
    grid.add_point(santa)
    grid.add_point(robo_santa)
    grid.increment(santa)
    grid.increment(robo_santa)

    print(grid)
    print()
    for idx, char in enumerate(directions):
        point = santa
        if idx % 2 != 0:
            point = robo_santa

        point.shift_direction_char(char)
        grid.increment(point)
        print(grid)
        print()

    for block in grid.data:
        for house in block:
            if house > 0:
                total += 1

    return total

if __name__ == "__main__":
    print(main())