def check(board, i, j):
    for x in range(9):
        if i == x: continue
        if board[x][j] == board[i][j]: return False
    
    for x in range(9):
        if j == x: continue
        if board[i][x] == board[i][j]: return False
        
    for x in range(i//3*3, i//3*3+3):
        for y in range(j//3*3, j//3*3+3):
            if x == i and y == j: continue
            if board[x][y] == board[i][j]: return False
    
    return True
    
def soln(board, i, j):
    if i>=9 or j>=9: return True
    if board[i][j] != '.':
        return soln(board, i+(j+1)//9, (j+1)%9)
    else:
        solved = False
        for n in range(1,10):
            board[i][j] = str(n)
            if check(board, i, j):
                res = soln(board, i+(j+1)//9, (j+1)%9)
                if res: 
                    solved = True
                    break
        if not solved:
            board[i][j] = '.'
        return solved


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        soln(board, 0, 0)
