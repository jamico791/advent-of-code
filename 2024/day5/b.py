import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def main():
    lines = read_lines(input_file)
    total = 0
    split_idx = lines.index("\n")
    lines = [line.rstrip("\n") for line in lines]
    ordering = lines[:split_idx]
    updates = lines[split_idx+1:]
    updates = [update.split(",") for update in updates]

    order_dict = {}
    for rule in ordering:
        nums = rule.split("|")
        if nums[0] in order_dict:
            order_dict[nums[0]].append(nums[1])
        else:
            order_dict[nums[0]] = [nums[1]]


    for update in updates:
        correct = True
        for idx, num in enumerate(update):
            new_idx = idx
            i = idx - 1
            while i >= 0:
                if num in order_dict.keys():
                    if update[i] in order_dict[num]:
                        new_idx = i
                        correct = False
                
                i -= 1
            update.pop(idx)
            update.insert(new_idx, num)

        if not correct:
            middle_idx = len(update) // 2
            total += int(update[middle_idx])

    return total

if __name__ == "__main__":
    print(main())