import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines_as_chars

input_file = "data.txt"

def main():
    lines = read_lines_as_chars(input_file)
    antenna_dict = {}
    antinode_set = set()

    for idy, line in enumerate(lines):
        for idx, char in enumerate(line):
            if char != ".":
                if char in antenna_dict.keys():
                    antenna_dict[char].append((idx, idy))
                else:
                    antenna_dict[char] = [(idx, idy)]

    for _, locations in antenna_dict.items():
        for i, location in enumerate(locations):
            for j in range(i+1, len(locations)):
                antinode1 = (location[0] + (location[0] - locations[j][0]), location[1] + (location[1] - locations[j][1]))
                antinode2 = (locations[j][0] + (locations[j][0] - location[0]), locations[j][1] + (locations[j][1] - location[1]))
                if antinode1[0] < len(lines[0]) and antinode1[1] < len(lines) and antinode1[0] >= 0 and antinode1[1] >= 0:
                    antinode_set.add(antinode1)
                if antinode2[0] < len(lines[0]) and antinode2[1] < len(lines) and antinode2[0] >= 0 and antinode2[1] >= 0:
                    antinode_set.add(antinode2)

    return len(antinode_set)

if __name__ == "__main__":
    print(main())