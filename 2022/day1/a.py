import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def main():
    lines = utility.read_lines(input_file)
    with open(input_file) as file:
        lines =  file.readlines()

    maximum = -999999
    curr = 0
    for line in lines:
        if line == "\n":
            if maximum < curr:
                maximum = curr
            curr = 0
        else:
            item_calories = int(line.rstrip("\n"))
            curr += item_calories

    return maximum


if __name__ == "__main__":
    print(main())