from typing import List

class Solution:
    def getRowRec(self, rowIndex: int) -> List[int]:
        
        # Helper function to compute Pascal's Triangle value
        def dfs(i: int, j: int) -> int:
            if j == 0 or j == i:
                return 1
            return dfs(i - 1, j - 1) + dfs(i - 1, j)
        
        # Generate the row by calling dfs for each element
        return [dfs(rowIndex, j) for j in range(rowIndex + 1)]
    
    def getRowIteratative(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
                print(row)
        
        return row

# Example usage
sol = Solution()

# Example 1
print(sol.getRowIteratative(3))  # Output: [1, 3, 3, 1]