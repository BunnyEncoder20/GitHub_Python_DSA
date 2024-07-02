def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                for num in '123456789':
                    if isPlaceable(board,i,j,num):
                        board[i][j]=num
                        if solveSudoku(board):
                            return True
                        else : 
                            board[i][j]="."
                return False             # could not place any number
    return True                          # No empty place left in the baord

def isPlaceable(board,row,col,num):
    for k in range(9):
        # check every col
        if board[row][k]==num : return False
        if board[k][col]==num : return False
        if board[3*(row//3)+(k//3)][3*(col//3)+(k%3)]==num : return False
    return True
    
if __name__ == "__main__":
    board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]
    solveSudoku(board)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()