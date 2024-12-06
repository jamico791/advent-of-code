import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def parse_lists(input_file):
    lines = ""
    list1 = []
    list2 = []
    
    lines = read_lines(input_file)
    for line in lines:
        tuple = line.rstrip("\n").split()
        list1.append(int(tuple[0]))
        list2.append(int(tuple[1]))

    return list1, list2

def main():
    list1, list2 = parse_lists(input_file)
    list1.sort()
    list2.sort()

    total = 0

    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    return total

if __name__ == "__main__":
    print(main())