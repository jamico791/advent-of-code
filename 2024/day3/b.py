import re
import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"
regex = r"mul\([\d]{1,3},[\d]{1,3}\)"
regex_b = r"(mul\([\d]{1,3},[\d]{1,3}\)|do\(\)|don't\(\))"

def do_multiply(string):
    nums = string.lstrip("mul(").rstrip(")").split(",")
    return int(nums[0]) * int(nums[1])
    

def main():
    lines = read_lines(input_file)
    matches = []
    total = 0
    do = True
    for line in lines:
        match_list = re.findall(regex_b, line)
        for match in match_list:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            
            elif do:
                total += do_multiply(match)

    return total


if __name__ == "__main__":
    print(main())