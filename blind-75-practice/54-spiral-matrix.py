from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        l, r, t, b = 0, COLS, 0, ROWS
        
        while l < r and b > t:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            
            # get every i in the   right column
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
            
            if not (l < r and t < b):
                break
            
            #- get every i in the bottom row
            for i in range(r-1, l -1, -1):
                res.append(matrix[b-1][i])
            b -=1
            
            # get every i in the left col
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            
        return res 

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))