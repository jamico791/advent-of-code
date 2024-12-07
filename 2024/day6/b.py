import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines
from utils.grids import Grid, Point
from utils.globals import Direction

input_file = "data.txt"

def traverse(grid, initial_guard_position):
    obstacle_positions = set()
    visited_set = set()
    has_loop = False

    guard = Point(initial_guard_position[0], initial_guard_position[1])
    grid.add_point(guard)
                
    og_width = grid.width
    og_height = grid.height

    while True:
        char = grid.get_value(guard)
        vector = Direction.char_to_vector(char)
        obstacle_positions.add((guard.x, guard.y))
        visited_value = (guard.x, guard.y, char)
        has_loop = visited_value in visited_set
        visited_set.add(visited_value)
        if grid.get_relative_value(guard, vector) == "#":
            grid.set_value(guard, Direction.vector_to_char(Direction.next_clockwise_cardinal(vector)))
        else:
            guard.shift(vector)
            grid.set_value(guard, char)
        if grid.width > og_width or grid.height > og_height or has_loop:
            break

    return obstacle_positions, has_loop

def main():
    lines = [list(line.rstrip("\n")) for line in read_lines(input_file)]
    intital_grid = Grid(lines=lines, infinite=True)
    initial_guard_position = None
    total = 0
    for i in range(intital_grid.height-1):
        for j in range(intital_grid.width-1):
            char = intital_grid.data[i][j]
            if char == "^" or char == ">" or char == "v" or char == "<":
                initial_guard_position = (j, i)
    
    obstacle_positions, has_loop = traverse(intital_grid, initial_guard_position)
    obstacle_positions.discard(initial_guard_position)
    for position in obstacle_positions:
        grid = Grid(lines=lines, infinite=True)
        grid.data[position[1]][position[0]] = "#"

        _, has_loop = traverse(grid, initial_guard_position)
        if has_loop:
            total += 1

    return total

if __name__ == "__main__":
    print(main())