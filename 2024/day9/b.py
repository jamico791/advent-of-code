import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line

input_file = "datacopy.txt"

def decode(string: str):
    block_representation = []
    id = 0
    for i, char in enumerate(string):
        block_representation.append([])
        for j in range(int(char)):
            if i % 2 == 0:
                block_representation[i].append(str(id))
                if j == int(char) - 1:
                    id += 1
            else:
                block_representation[i].append(".")

    return block_representation

def finalize(representation):
    final = []
    for block in representation:
        for num in block:
            final.append(num)

    return final

def main():
    line = read_first_line(input_file).rstrip("\n")
    block_representation = decode(line)
    total = 0

    i = len(block_representation) - 1
    while i >= 0:
        if "." not in block_representation[i] and block_representation[i] != []:
            j = 1
            while j < i and len(block_representation[j]) < len(block_representation[i]) :
                j += 2
            if j < i:
                block_representation[j] = block_representation[j][len(block_representation[i]):]
                block = block_representation.pop(i)
                block_representation.insert(j, block)
                right_space = 0
                if i + 1 < len(block_representation):
                    right_space = len(block_representation[i+1])
                    block_representation.pop(i+1)
                for _ in range(len(block)+right_space):
                    block_representation[i].append(".")
                block_representation.insert(j, [])
                i += 1
        i -= 1

    total = 0
    for idx, num in enumerate(finalize(block_representation)):
        if num != ".":
            total += idx * int(num)

    return total


if __name__ == "__main__":
    print(main())