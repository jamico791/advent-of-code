import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def parse_reports(input_file):
    lines = ""
    reports = []
    
    with open(input_file) as file:
        lines = file.readlines()

    for line in lines:
        report = line.rstrip("\n").split()
        reports.append(report)

    return reports

def find_unsafe_index(report):
    prev = report[0]
    asc = "Null"
    i = 1
    is_unsafe = False

    while i < len(report) and not is_unsafe:
        diff = int(report[i]) - int(prev)
        curr_asc = diff > 0
        if asc == "Null":
            asc = diff > 0
        elif asc != curr_asc:
            is_unsafe = True

        if diff == 0:
            is_unsafe = True
        if abs(diff) < 1 or abs(diff) > 3:
            is_unsafe = True

        prev = report[i]
        i += 1
    
    if is_unsafe:
        return i - 1
    
    return -1

def main():
    reports = parse_reports(input_file)
    safe_count = 0

    for report in reports:
        prev = report[0]
        asc = "Null"
        i = 1
        is_unsafe = False

        while i < len(report) and not is_unsafe:
            diff = int(report[i]) - int(prev)
            curr_asc = diff > 0
            if asc == "Null":
                asc = diff > 0
            elif asc != curr_asc:
                is_unsafe = True

            if diff == 0:
                is_unsafe = True
            if abs(diff) < 1 or abs(diff) > 3:
                is_unsafe = True

            prev = report[i]
            i += 1
        
        if not is_unsafe:
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    print(main())