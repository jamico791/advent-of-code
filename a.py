import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "example.txt"

def main():
    lines = read_lines(input_file)
    for line in lines:
        pass

    return None

if __name__ == "__main__":
    print(main())