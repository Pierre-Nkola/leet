class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) -1
        
        for i in range(len(nums) -1, -1 , -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
                
        
        
        
sol = Solution()

print(sol.canJump(nums = [2,3,1,1,4]))