class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre_prod = 1
        suf_prod = 1
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = pre_prod
            pre_prod *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suf_prod
            suf_prod *= nums[j]
        return res



sol = Solution()
