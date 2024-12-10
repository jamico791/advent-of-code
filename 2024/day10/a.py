import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines_as_ints
from utils.grids import Grid, Point

input_file = "data.txt"

def hike(map: Grid, hiker: Point, current_elev: int, visited: set):
    current_location = (hiker.x, hiker.y)
    next_steps = map.get_relative_cardinal_values(hiker)
    summit_count = 0

    if current_elev == 9:
        visited.add(current_location)
        return 1
    if not current_elev + 1 in next_steps.values():
        return 0
    for direction, elev in next_steps.items():
        if elev == current_elev + 1:
            hiker.move(current_location[0], current_location[1])
            hiker.shift(direction)
            summit_count += hike(map, hiker, current_elev + 1, visited)
    
    return summit_count

def main():
    lines = read_lines_as_ints(input_file)
    map = Grid(lines=lines)
    hiker = Point(0, 0)

    map.add_point(hiker)
    trailheads = map.find_all(0)
    total = 0
    for trailhead in trailheads:
        hiker.move(trailhead[0], trailhead[1])
        visited = set()
        hike(map, hiker, map.get_value(hiker), visited)
        total += len(visited)

    return total

if __name__ == "__main__":
    print(main())