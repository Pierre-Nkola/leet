from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        fresh_oranges = 0
        rotten_queue = collections.deque()
        
        # Initialize the count of fresh oranges and add all rotten oranges to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        # Early exit if there are no fresh oranges
        if fresh_oranges == 0:
            return 0
        
        # Perform BFS from initially rotten oranges
        minutes_passed = 0
        while rotten_queue:
            minutes_passed += 1
            for _ in range(len(rotten_queue)):
                row, col = rotten_queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        # Mark the orange as rotten
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        rotten_queue.append((nr, nc))
        
        # If there are still fresh oranges left, return -1
        return minutes_passed - 1 if fresh_oranges == 0 else -1

# Example usage
sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output should be 4
