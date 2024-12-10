import hashlib
import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

from utils.files import read_first_line

input_file = "data.txt"

def main():
    secret_key = read_first_line(input_file)
    first_five = ""
    i = 0
    while first_five != "00000":
        i += 1
        combined_keys = secret_key + str(i)
        first_five = hashlib.md5(combined_keys.encode()).hexdigest()[:5]

    return i

if __name__ == "__main__":
    print(main())