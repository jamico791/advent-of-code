import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines_as_chars

input_file = "data.txt"

def main():
    lines = read_lines_as_chars(input_file)
    total = 0
    for line in lines:
        double_set = set()
        skip_repeat = False
        double_double = False
        for i, char in enumerate(line):
            if i < len(line) - 2:
                if not skip_repeat and line[i+2] == char:
                    skip_repeat = True
                if not (line[i+1] == char and line[i+2] == char):
                    if (line[i] + line[i+1]) in double_set:
                        double_double = True
                    else:
                        double_set.add(line[i] + line[i+1])
            elif i < len(line) - 1 :
                if (line[i] + line[i+1]) in double_set:
                    double_double = True
                else:
                    double_set.add(line[i] + line[i+1])
        if double_double and skip_repeat:
            total += 1

    return total

if __name__ == "__main__":
    print(main())