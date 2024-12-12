"""Various utilities for Advent of Code"""

def read_first_line(input_file):
    with open(input_file, "r") as file:
        line = file.readline()
        
    return line

def read_lines(input_file):
    with open(input_file, "r") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    return lines

def read_lines_as_chars(input_file):
    lines = [list(line) for line in read_lines(input_file)]

    return lines

def read_lines_as_ints(input_file):
    lines = [[int(char) for char in list(line)] for line in read_lines(input_file)]

    return lines

def read_specific_line(input_file, line_num: int):
    lines = read_lines(input_file)
    
    return lines[line_num - 1]

if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            print(i, j)