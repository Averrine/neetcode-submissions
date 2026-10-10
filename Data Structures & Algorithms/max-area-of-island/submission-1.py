class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def eplo(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0 

            grid[r][c] = 0
            return (1
                + eplo(r +1, c)
                + eplo(r -1, c)
                + eplo(r, c + 1)
                + eplo(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, eplo(r,c))
        return maxArea