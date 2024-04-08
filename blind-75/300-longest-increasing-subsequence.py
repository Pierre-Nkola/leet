class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [1] * (len(nums))
        for i in range(len(nums) -1, -1, -1):
            for j in range (i+1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)
                    

sol = Solution()

print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))


print([1]*5)