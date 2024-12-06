import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def main():
    lines = read_lines(input_file)
    split_idx = lines.index("\n")
    lines = [line.rstrip("\n") for line in lines]
    ordering = lines[:split_idx]
    updates = lines[split_idx+1:]

    order_dict = {}
    for rule in ordering:
        nums = rule.split("|")
        if nums[0] in order_dict:
            order_dict[nums[0]].append(nums[1])
        else:
            order_dict[nums[0]] = [nums[1]]

    updates = [update.split(",") for update in updates]

    total = 0

    for update in updates:
        correct = True
        for idx, num in enumerate(update):
            i = idx - 1
            while i >= 0:
                if num in order_dict.keys():
                    if update[i] in order_dict[num]:
                        correct = False
                
                i -= 1
        if correct:
            middle_idx = len(update) // 2
            total += int(update[middle_idx])


    return total

if __name__ == "__main__":
    print(main())