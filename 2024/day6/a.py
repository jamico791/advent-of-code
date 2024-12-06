import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))


import utility

input_file = "data.txt"

def main():
    lines = utility.read_lines(input_file)
    grid = utility.Grid(lines=lines, infinite=True)
    total = 0
    pointer_name = "guard"
    grid.add_pointer(pointer_name, utility.Color.red.value)
    for i in range(grid.height-1):
        for j in range(grid.width-1):
            char = grid.data[i][j]
            if char == "^" or char == ">" or char == "v" or char == "<":
                grid.move_pointer(pointer_name, j+1, i+1)
    og_width = grid.width
    og_height = grid.height

    while grid.width <= og_width and grid.height <= og_height:
        if grid.get_pointer_value(pointer_name) == "^":
            grid.set_pointer_value(pointer_name, "X")
            grid.north(pointer_name)
            if grid.get_pointer_value(pointer_name) == "#":
                grid.south(pointer_name)
                grid.set_pointer_value(pointer_name, ">")
            else:
                grid.set_pointer_value(pointer_name, "^")
        elif grid.get_pointer_value(pointer_name) == ">":
            grid.set_pointer_value(pointer_name, "X")
            grid.east(pointer_name)
            if grid.get_pointer_value(pointer_name) == "#":
                grid.west(pointer_name)
                grid.set_pointer_value(pointer_name, "v")
            else:
                grid.set_pointer_value(pointer_name, ">")
        elif grid.get_pointer_value(pointer_name) == "v":
            grid.set_pointer_value(pointer_name, "X")
            grid.south(pointer_name)
            if grid.get_pointer_value(pointer_name) == "#":
                grid.north(pointer_name)
                grid.set_pointer_value(pointer_name, "<")
            else:
                grid.set_pointer_value(pointer_name, "v")
        elif grid.get_pointer_value(pointer_name) == "<":
            grid.set_pointer_value(pointer_name, "X")
            grid.west(pointer_name)
            if grid.get_pointer_value(pointer_name) == "#":
                grid.east(pointer_name)
                grid.set_pointer_value(pointer_name, "^")
            else:
                grid.set_pointer_value(pointer_name, "<")
    for row in grid.data:
        for char in row:
            if char == "X":
                total += 1

    return total

if __name__ == "__main__":
    print(main())