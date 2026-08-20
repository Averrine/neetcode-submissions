class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
       # define the safe checking function 
       # initialize a table of n x n 
       # backtracking function 
       # return safe queens on board 

        def safe(board, row, col, n):
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            
            for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            return True

        
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def backtrack(board, col):
            if col == n:
                result.append([''.join(row) for row in board])
                return
            for i in range(n):
                if safe(board, i, col, n):
                    board[i][col] = 'Q'
                    backtrack(board, col + 1)
                    board[i][col] = '.'
        backtrack(board, 0)
        return result

