import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def find(board, row, col):
    if row < 0 or row >= len(board[0]) or col < 0 or col >= len(board[0]):
        return 0
    return board[row][col]

def main():
    board = utility.read_lines(input_file)
    total = 0
    for i in range(len(board)):
        board[i] = board[i].rstrip("\n")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "A":
                ne = find(board, i-1, j+1) #NE
                se = find(board, i+1, j+1) #SE
                sw = find(board, i+1, j-1) #SW
                nw = find(board, i-1, j-1) #NW
                nwse_diag = [nw, se]
                nesw_diag = [ne, sw]
                if ("M" in nwse_diag and "S" in nwse_diag) and ("M" in nesw_diag and "S" in nesw_diag):
                    total += 1

    return total

if __name__ == "__main__":
    print(main())