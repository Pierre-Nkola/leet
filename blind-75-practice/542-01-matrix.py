from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initialize distances and add all 0 cells to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')

        # BFS from all 0 cells
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat

# Example usage:
sol = Solution()
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]
print(sol.updateMatrix(mat))
