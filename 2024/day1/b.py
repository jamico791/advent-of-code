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

    hashmap = {}
    for num in list2:
        if num in hashmap.keys():
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    
    similarity_score = 0
    for num in list1:
        if num in hashmap.keys():
            similarity_score += hashmap[num] * num

    return similarity_score

if __name__ == "__main__":
    print(main())