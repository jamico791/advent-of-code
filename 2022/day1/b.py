import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def main():
    lines = read_lines(input_file)

    count = 0
    elf_list = []

    for i in range(len(lines)):
        if i == len(lines) - 1:
            count += int(lines[i].rstrip("\n"))
            elf_list.append(count)
            count = 0

        if lines[i] == "\n":
            elf_list.append(count)
            count = 0
        else:
            count += int(lines[i].rstrip("\n"))

    elf_list.sort(reverse=True)
    elf_list = elf_list[:3]
    return sum(elf_list)



if __name__ == "__main__":
    print(main())