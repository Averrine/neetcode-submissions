class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0


        def explore(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            return (1 
                + explore(r+1,c) 
                + explore(r-1,c) 
                + explore(r,c+1) 
                + explore(r,c-1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, explore(r, c))

        return maxArea


            

