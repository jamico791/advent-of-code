import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_lines

input_file = "data.txt"

def main():
    lines = [line.rstrip("\n") for line in read_lines(input_file)]
    total = 0

    for line in lines:
        split_line = line.split(":")
        test_value = int(split_line[0])
        equation_numbers = [int(num) for num in split_line[1].lstrip().split(" ")]
        results = [[]]
        equation_numbers_pointer = 2
        results_pointer = 1
        results[0] = [equation_numbers[0] + equation_numbers[1], equation_numbers[0] * equation_numbers[1]]
        while equation_numbers_pointer < len(equation_numbers):
            results.append([])
            for result in results[results_pointer-1]:
                results[results_pointer].append(result + equation_numbers[equation_numbers_pointer])
                results[results_pointer].append(result * equation_numbers[equation_numbers_pointer])
            results_pointer += 1
            equation_numbers_pointer += 1
        if test_value in results[-1]:
            total += test_value
    return total

if __name__ == "__main__":
    print(main())