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
        dimensions.sort()
        volume = dimensions[0] * dimensions[1] * dimensions[2]
        total += dimensions[0] * 2 + dimensions[1] * 2 + volume

    return total


if __name__ == "__main__":
    print(main())