import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def main():
    lines = utility.read_lines(input_file)
    lines = [line.rstrip("\n") for line in lines]
    total = 0
    combinations = len(lines) * len(lines[0])
    counter = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            direction_mapping = [[{""} for char in line] for line in lines]
            counter += 1
            loop_detected = False
            print(f"{counter}/{combinations}")
            grid = utility.Grid(lines=lines, infinite=True)
            pointer_name = "guard"
            grid.add_pointer(pointer_name, utility.Color.red.value)
            pointer = grid.get_pointer(pointer_name)
            for k in range(grid.height):
                for l in range(grid.width):
                    char = grid.data[k][l]
                    if char == "^" or char == ">" or char == "v" or char == "<":
                        grid.move_pointer(pointer_name, l+1, k+1)
                        direction_mapping[k][l].add(char)

            og_width = grid.width
            og_height = grid.height

            if i != pointer.y-1 or j != pointer.x-1:
                grid.data[i][j] = "O"
            while True:
                if grid.get_pointer_value(pointer_name) == "^":
                    grid.set_pointer_value(pointer_name, "X")
                    grid.north(pointer_name)
                    if grid.get_pointer_value(pointer_name) == "#" or grid.get_pointer_value(pointer_name) == "O":
                        grid.south(pointer_name)
                        grid.set_pointer_value(pointer_name, ">")
                    else:
                        grid.set_pointer_value(pointer_name, "^")
                elif grid.get_pointer_value(pointer_name) == ">":
                    grid.set_pointer_value(pointer_name, "X")
                    grid.east(pointer_name)
                    if grid.get_pointer_value(pointer_name) == "#" or grid.get_pointer_value(pointer_name) == "O":
                        grid.west(pointer_name)
                        grid.set_pointer_value(pointer_name, "v")
                    else:
                        grid.set_pointer_value(pointer_name, ">")
                elif grid.get_pointer_value(pointer_name) == "v":
                    grid.set_pointer_value(pointer_name, "X")
                    grid.south(pointer_name)
                    if grid.get_pointer_value(pointer_name) == "#" or grid.get_pointer_value(pointer_name) == "O":
                        grid.north(pointer_name)
                        grid.set_pointer_value(pointer_name, "<")
                    else:
                        grid.set_pointer_value(pointer_name, "v")
                elif grid.get_pointer_value(pointer_name) == "<":
                    grid.set_pointer_value(pointer_name, "X")
                    grid.west(pointer_name)
                    if grid.get_pointer_value(pointer_name) == "#" or grid.get_pointer_value(pointer_name) == "O":
                        grid.east(pointer_name)
                        grid.set_pointer_value(pointer_name, "^")
                    else:
                        grid.set_pointer_value(pointer_name, "<")

                if grid.width > og_width or grid.height > og_height:
                    break
                if grid.get_pointer_value(pointer_name) in direction_mapping[pointer.y-1][pointer.x-1]:
                    loop_detected = True
                direction_mapping[pointer.y-1][pointer.x-1].add(grid.get_pointer_value(pointer_name))
                

                if loop_detected:
                    total += 1
                    break

    return total

if __name__ == "__main__":
    print(main())