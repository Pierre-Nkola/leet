class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) -1
        res = nums[l]

        while l <= r:

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[(l+r)//2])
            if nums[(l+r)//2] >= nums[l]:
                l = (l+r)//2 +1

            else:
                r = ((l+r)//2) -1
        return res


sol = Solution()

sol_res = sol.findMin(nums = [3,1,2])

print(sol_res)