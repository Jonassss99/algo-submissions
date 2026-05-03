class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        # using dfs to make adjacent '1's be '0's
        def dfs(r, c):
            # edge case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # mark as '0'
            grid[r][c] = '0'
            
            # define 4 directions
            dfs(r + 1, c) 
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1) 

        # iterate over the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1  # update island
                    dfs(r, c)     # eliminate island    
                    
        return islands    
        