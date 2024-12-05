import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def main():
    directions = utility.read_first_line(input_file)
    final_floor = 0
    for i in range(len(directions)):
        if directions[i] == "(":
            final_floor += 1
        elif directions[i] == ")":
            final_floor -= 1

        if final_floor < 0:
            return i + 1

    return -1

if __name__ == "__main__":
    print(main())