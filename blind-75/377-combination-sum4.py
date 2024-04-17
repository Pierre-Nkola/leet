class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {0:1}
        
        for total in range(1, total+1):
            dp[total] = 0
            
            for n in nums:
                dp[total] = dp.get(total-n, 0)
        
        return dp[target]
    
sol = Solution()

print(sol.combinationSum4(nums = [1,2,3], target = 4))