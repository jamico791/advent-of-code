import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_specific_line
from utils.trees import Tree

input_file = "data.txt"

def main():
    line = read_specific_line(input_file, 1)
    rocks = line.split()
    num_blinks = 75
    rock_map = {}

    for rock in rocks:
        rock_map[rock] = 1 if rock not in rock_map.keys() else rock_map[rock] + 1

    for blink_count in range(num_blinks):
        temp_map = {}
        for rock, rock_count in rock_map.items():
            if rock == "0":
                temp_map["1"] = 1 * rock_count if "1" not in temp_map.keys() else temp_map["1"] + (1 * rock_count)
            elif len(rock) % 2 == 0:
                middle = len(rock) // 2
                left_half = str(int(rock[:middle]))
                right_half = str(int(rock[middle:]))
                temp_map[right_half] = 1 * rock_count if right_half not in temp_map.keys() else temp_map[right_half] + (1 * rock_count)
                temp_map[left_half] = 1 * rock_count if left_half not in temp_map.keys() else temp_map[left_half] + (1 * rock_count)
            else:
                temp_map[str(int(rock) * 2024)] = 1 * rock_count if str(int(rock) * 2024) not in temp_map.keys() else temp_map[str(int(rock) * 2024)] + (1 * rock_count)
        rock_map = temp_map

    total = 0
    for amount in rock_map.values():
        total += amount


    return total

if __name__ == "__main__":
    print(main())