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

from typing import List, Set, Tuple

def print_board(board: List[list]) -> None:
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

def find_empty_spot(board: List[list], empty_value=0) -> Tuple[int, int]:
    """
    Shall return None if the board is full. 
    Set empty_value for easy test (and allow other value such as * or _)
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == empty_value:
                return (i, j)

def check_is_valid(board: List[list], num: int, position: Tuple[int, int]) -> bool:
    # check row
    x, y = position
    for j in range(len(board[0])):
        if board[x][j] == num and j != y:
            return False
    # check columns
    for i in range(len(board)):
        if board[i][y] == num and i != x:
            return False
    # check box
    box_x = x // 3
    box_y = y // 3
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y *3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False
    return True

def solve(board: List[list]):
    # base case:
    to_visit = find_empty_spot(board)
    if to_visit:
        row, col = to_visit
    else: # no remaining empty spot, solved.
        return True

    for candidate_value in range(1,10):
        if check_is_valid(board, candidate_value, (row, col)):
            board[row][col] = candidate_value

            if solve(board):
                return True
            
            board[row][col] = 0
    return False

# Main
print_board(board)

# hand test:
assert check_is_valid(board, 5, (1,1)) == False
assert check_is_valid(board, 1, (1,1)) == True
assert check_is_valid(board, 1, (8,8)) == False
assert find_empty_spot(board, -1) == None

print()
solve(board)
print_board(board)