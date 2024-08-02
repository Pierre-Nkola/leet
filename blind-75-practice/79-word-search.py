from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS , COLS= len(board), len(board[0])
        path = set()
        
        def dfs(r,c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or (r,c) in path
                or c >= COLS or board[r][c] != word[i]):
                return False
            
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                dfs(r, c-1, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c-1, i+1))
            path.remove((r,c))
            
            for i in range(ROWS):
                for j in range(COLS):
                    if dfs(r,c,0): return True
            return False
            
            