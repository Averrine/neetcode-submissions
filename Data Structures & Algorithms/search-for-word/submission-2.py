class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # defining the values for rows and columns 
        rows, cols = len(board), len(board[0])
        # helper function using depth first search
        def dfs(r, c, i):
            # if the index of word is equal to the length of word return true
            if i == len(word):
                return True
            # if r or c are less than 0, if r or c are more or equal to rows and cols or if current place on board
            # isnt equal to current value of word return false 
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] ):
                return False
            
            # setting up temporary value
            temp = board[r][c]
            # when a value is explore place a # on board
            board[r][c] = '#'

            # found is the movement towards the next letter
            found = (
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1)
            )

            # backtracking 
            board[r][c] = temp
            # returns the found value
            return found
        # final loop: loops through rows and cols using dfs, returns true if word found else false
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True 
        return False