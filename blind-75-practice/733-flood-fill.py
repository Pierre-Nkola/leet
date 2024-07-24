from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])        
        originalColor = image[sr][sc]
        
        if originalColor == color:
            return image
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
        
            if image[sr][sc] != originalColor:
                return
            
            image[r][c] = color
            self.dfs(r+1,c)
            self.dfs(r,c+1)
            self.dfs(r-1,c)
            self.dfs(r,c-1)