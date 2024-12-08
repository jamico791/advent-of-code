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
                difference_vector = (location[0] - locations[j][0], location[1] - locations[j][1])
                antinode_set.add(location)

                next_dir1 = (location[0], location[1])
                while next_dir1[0] < len(lines[0]) and next_dir1[0] < len(lines) and next_dir1[0] >= 0 and next_dir1[1] >= 0:
                    if next_dir1[0] < len(lines[0]) and next_dir1[1] < len(lines) and next_dir1[0] >= 0 and next_dir1[1] >= 0:
                        antinode_set.add(next_dir1)
                    next_dir1 = (next_dir1[0] + difference_vector[0], next_dir1[1] + difference_vector[1])

                next_dir2 = (locations[j][0], locations[j][1])
                while next_dir2[0] < len(lines[0]) and next_dir2[0] < len(lines) and next_dir2[0] >= 0 and next_dir2[1] >= 0:
                    if next_dir2[0] < len(lines[0]) and next_dir2[1] < len(lines) and next_dir2[0] >= 0 and next_dir2[1] >= 0:
                        antinode_set.add(next_dir2)
                    next_dir2 = (next_dir2[0] - difference_vector[0], next_dir2[1] - difference_vector[1])
                
                

    return len(antinode_set)

if __name__ == "__main__":
    print(main())