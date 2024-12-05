import sys, os
current_file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_file_path)
sys.path.append(os.path.abspath(os.path.join('..', '..')))

import utility

input_file = "data.txt"

def find(board, word, row, col, vdir, hdir, i=0):
    if i == len(word):
        return 1

    if row < 0 or row >= len(board[0]) or col < 0 or col >= len(board[0]):
        return 0
    
    if board[row][col] == "XMAS"[i]:
        return find(board, word, row + vdir, col + hdir, vdir, hdir, i + 1)

    return 0
    


def main():
    board = utility.read_lines(input_file)
    total = 0
    for i in range(len(board)):
        board[i] = board[i].rstrip("\n")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                total += find(board, "XMAS", i, j, -1, 0) #N
                total += find(board, "XMAS", i, j, -1, 1) #NE
                total += find(board, "XMAS", i, j, 0, 1) #E
                total += find(board, "XMAS", i, j, 1, 1) #SE
                total += find(board, "XMAS", i, j, 1, 0) #S
                total += find(board, "XMAS", i, j, 1, -1) #SW
                total += find(board, "XMAS", i, j, 0, -1) #W
                total += find(board, "XMAS", i, j, -1, -1) #NW
        

    return total

if __name__ == "__main__":
    print(main())