class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # 1 is land 
    # 0 is water 
    
    # count = 0
    # For each cell (r, c) in the grid:
    #   if the cell is land and not visited:
    #       count += 1
    #       explore entire island from (r, c):
    #           mark the cell visited "#"
    #           for each of the 4 members:
    #               if in bounds, not visited, and is island:
    #                   explore from that neighbor
    # return count
        rows, cols = len(grid), len(grid[0])
        count = 0


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
                    count +=1
                    explore(r, c)
        return count



                    


