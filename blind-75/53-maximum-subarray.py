class Solution:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -2**31
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now

sol = Solution()

sol_res = sol.maxSubArray(nums = [1,1,1,-1,1,1])
# sol_res = sol.maxSubArray(nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4])

print(sol_res)
