class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    # Check if adjacent cell above is land
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # Check if adjacent cell to the left is land
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter
