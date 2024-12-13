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
        vowel_count = 0
        double = False
        bad_double = False
        for i, char in enumerate(line):
            if char in "aeiou":
                vowel_count += 1
            if i < len(line) - 1:
                if ((char == "a" and line[i+1] == "b") or \
                   (char == "c" and line[i+1] == "d") or \
                   (char == "p" and line[i+1] == "q") or \
                   (char == "x" and line[i+1] == "y")):
                    bad_double = True
                if not double and line[i+1] == char:
                    double = True
        if vowel_count >= 3 and double and not bad_double:
            total += 1

    return total

if __name__ == "__main__":
    print(main())