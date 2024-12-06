"""Various utilities for Advent of Code"""

def read_first_line(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        
    return line

def read_lines(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    return lines


if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            print(i, j)