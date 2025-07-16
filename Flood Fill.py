class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # If the new color is the same as the original, no change needed
        if original_color == color:
            return image
        
        def dfs(r, c):
            # Check bounds and if current pixel has the original color
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != original_color):
                return
            
            # Change the color of current pixel
            image[r][c] = color
            
            # Recursively fill in all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        dfs(sr, sc)
        return image
