import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines
from utils.grids import Grid, Point
from utils.globals import Color, Direction

input_file = "data.txt"

def main():
    lines = read_lines(input_file)
    lines = [line.rstrip("\n") for line in lines]
    total = 0

    grid = Grid(lines=lines, infinite=True)
    guard = Point(0, 0)
    grid.add_point(guard)
    for i in range(grid.height-1):
        for j in range(grid.width-1):
            char = grid.data[i][j]
            if char == "^" or char == ">" or char == "v" or char == "<":
                guard.move(j, i)
                
    og_width = grid.width
    og_height = grid.height

    while grid.width <= og_width and grid.height <= og_height:
        char = grid.get_value(guard)
        vector = Direction.char_to_vector(char)
        grid.set_value(guard, "X")
        if grid.get_relative_value(guard, vector) == "#":
            grid.set_value(guard, Direction.vector_to_char(Direction.next_clockwise_cardinal(vector)))
        else:
            guard.shift(vector)
            grid.set_value(guard, char)
        
    for row in grid.data:
        for char in row:
            if char == "X":
                total += 1

    return total

if __name__ == "__main__":
    print(main())