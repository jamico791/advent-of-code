import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

sys.setrecursionlimit(10000)

from utils.files import read_lines_as_chars
from utils.grids import Grid, Point, Region
from utils.globals import Color

input_file = "data.txt"

def discover(char, current_location, locations, lines):
    if current_location not in locations:
        locations.append(current_location)
        # North
        if current_location[1] > 0 and lines[current_location[1] - 1][current_location[0]] == char:
            discover(char, (current_location[0], current_location[1] - 1), locations, lines)
        # East
        if current_location[0] < len(lines[0]) - 1 and lines[current_location[1]][current_location[0] + 1] == char:
            discover(char, (current_location[0] + 1, current_location[1]), locations, lines)
        # South
        if current_location[1] < len(lines) - 1 and lines[current_location[1] + 1][current_location[0]] == char:
            discover(char, (current_location[0], current_location[1] + 1), locations, lines)
        # West
        if current_location[0] > 0 and lines[current_location[1]][current_location[0] - 1] == char:
            discover(char, (current_location[0] - 1, current_location[1]), locations, lines)

    return
    
def get_neighbor_values(location, lines):
    neighbors = [None, None, None, None]
    # North
    if location[1] > 0:
        neighbors[0] = lines[location[1] - 1][location[0]]
    # East
    if location[0] < len(lines[0]) - 1:
        neighbors[1] = lines[location[1]][location[0] + 1] 
    # South
    if location[1] < len(lines) - 1:
        neighbors[2] = lines[location[1] + 1][location[0]] 
    # West
    if location[0] > 0:
        neighbors[3] = lines[location[1]][location[0] - 1]

    return neighbors

def main():
    lines = read_lines_as_chars(input_file)
    hashmap = {}

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            char = lines[y][x]
            already_used = False
            if char not in hashmap.keys():
                hashmap[char] = []
            else:
                for region in hashmap[char]:
                    if (x, y) in region:
                        already_used = True

            if not already_used:
                locations = []
                discover(char, (x, y), locations, lines)
                hashmap[char].append(locations)

    total = 0
    for char, region_list in hashmap.items():
        for region in region_list:
            area = 0
            side_count = 0
            edge_list = {}
            for location in region:
                area += 1
                neighbors = get_neighbor_values(location, lines)
                if neighbors[0] != char:
                    edge_name = str(location[1]) + "N"
                    if edge_name not in edge_list.keys():
                        edge_list[edge_name] = []
                    edge_list[edge_name].append(location[0])
                if neighbors[1] != char:
                    edge_name = str(location[0]) + "E"
                    if edge_name not in edge_list.keys():
                        edge_list[edge_name] = []
                    edge_list[edge_name].append(location[1])
                if neighbors[2] != char:
                    edge_name = str(location[1]) + "S"
                    if edge_name not in edge_list.keys():
                        edge_list[edge_name] = []
                    edge_list[edge_name].append(location[0])
                if neighbors[3] != char:
                    edge_name = str(location[0]) + "W"
                    if edge_name not in edge_list.keys():
                        edge_list[edge_name] = []
                    edge_list[edge_name].append(location[1])
            for arr in edge_list.values():
                arr.sort()
                i = 1
                while i < len(arr):
                    if arr[i - 1] < arr[i] - 1:
                        side_count += 1
                    i += 1
                side_count += 1

            total += area * side_count
                    
    return total

if __name__ == "__main__":
    print(main())