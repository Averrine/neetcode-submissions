class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        counter = 0


        def explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return 

            grid[r][c] = "0"
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    counter += 1
                    explore(r,c)
        return counter
