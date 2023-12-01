class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])

        island_count = 0

        def conquer(x, y):
            grid[x][y] = '0'

            if x > 0 and grid[x-1][y] == '1':
                conquer(x-1,y)
            if y + 1 < m and grid[x][y+1] == '1':
                conquer(x,y+1)
            if x + 1 < n and grid[x+1][y] == '1':
                conquer(x+1,y)
            if y > 0 and grid[x][y-1] == '1':
                conquer(x,y-1)
    
        for i, row in enumerate(grid):
            for j, plot in enumerate(row):
                if plot == "0":
                    continue
                
                island_count += 1

                conquer(i,j)

        return island_count

