class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # identifying rows and cols
        rows, cols = len(board), len(board[0])

        # definining depth first search function
        def dfs(r, c, i):
            if i == len(word):
                return True
            # accounts for out of bound or already used 
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]):
                return False
            
            #marking visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore up, down, left, right
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            board[r][c] = temp

            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        
