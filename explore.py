board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("- " * 12)
        for j in range (len(board[0])):
            if board[i][j] != 0:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
            if (j+1) % 3 == 0 and j != 0:
                print("|", end=" ")
        print("")

def find_empty_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

print_board(board)