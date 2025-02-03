def n_queen(n):
    board = [[0 for i in range(n)] for j in range(n)]

    if solve_until(board, 0) == False:
        print("No Solution")
        return  

    print_board(board)

def solve_until(board, col):
    if col >= len(board):  
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_until(board, col + 1) == True:
                return True  
            
            board[i][col] = 0  

    return False  

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                print(".", end=" ")
            elif board[i][j] == 1:
                print("Q", end=" ")
        print()

n = int(input("Enter the Dimension of Board-> "))
n_queen(n)
