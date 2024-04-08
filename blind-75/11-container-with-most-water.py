class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        l, r = 0, len(height) -1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, area)
            if height[l] <= height[r]:
                l +=1
            else:
                r -=1
        return max_water
    
sol = Solution()

print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))

            