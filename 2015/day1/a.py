import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def main():
    directions = utility.read_first_line(input_file)
    final_floor = 0
    for char in directions:
        if char == "(":
            final_floor += 1
        elif char == ")":
            final_floor -= 1

    return final_floor

if __name__ == "__main__":
    print(main())