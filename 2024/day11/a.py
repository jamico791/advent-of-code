import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_specific_line

input_file = "data.txt"

def main():
    line = read_specific_line(input_file, 1)
    rocks = line.split()
    num_blinks = 25

    skip = 0
    for blink_count in range(num_blinks):
        for i, rock in enumerate(rocks):
            if skip <= 0:
                if rock == "0":
                    rocks[i] = "1"
                elif len(rock) % 2 == 0:
                    middle = len(rock) // 2
                    left_half = str(int(rock[:middle]))
                    right_half = str(int(rock[middle:]))
                    rocks[i] = right_half
                    rocks.insert(i, left_half)
                    skip = 1
                else:
                    rocks[i] = str(int(rock) * 2024)
            else:
                skip -= 1

    return len(rocks)

if __name__ == "__main__":
    print(main())