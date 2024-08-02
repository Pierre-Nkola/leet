from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) -1
        
        while l < r:
            maxArea = max(maxArea, min(height[r], height[l]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
                
sol = Solution()

print(sol.maxArea(height = [1,1]))