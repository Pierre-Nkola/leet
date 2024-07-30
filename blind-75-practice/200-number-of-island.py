from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        island = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for sr,sc in directions:
                    nr = row + sr
                    nc = col + sc
                    
                    if (nr in range(ROWS) and nc in range(COLS) and
                        grid[nr][nc] == "1" and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1                    
                    
        return island
                    
sol = Solution()

print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))