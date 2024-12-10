import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line

input_file = "data.txt"

def decode(string: str):
    block_representation = []
    id = 0
    for i, char in enumerate(string):
        for j in range(int(char)):
            if i % 2 == 0:
                block_representation.append(str(id))
                if j == int(char) - 1:
                    id += 1
            else:
                block_representation += "."


    return block_representation


def main():
    line = read_first_line(input_file).rstrip("\n")
    block_representation = decode(line)
    char_list = block_representation

    i = 0
    while i < len(char_list):
        if char_list[i] == ".":
            end_pointer = -1
            while char_list[end_pointer] == ".":
                char_list.pop(end_pointer)
            char_list.insert(i, char_list.pop(end_pointer))
            if i + 1 < len(char_list):
                char_list.pop(i + 1)
        i += 1

    total = 0
    for idx, num in enumerate(char_list):
        total += idx * int(num)

    return total

if __name__ == "__main__":
    print(main())