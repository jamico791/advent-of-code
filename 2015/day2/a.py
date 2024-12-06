import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def main():
    lines = read_lines(input_file)
    total = 0
    for line in lines:
        dimensions = line.rstrip("\n").split("x")
        dimensions = list(map(int, dimensions))
        side1 = dimensions[0] * dimensions[1]
        side2 = dimensions[1] * dimensions[2]
        side3 = dimensions[0] * dimensions[2]
        total += side1 * 2 + side2 * 2 + side3 * 2 + min(side1, side2, side3)

    return total


if __name__ == "__main__":
    print(main())