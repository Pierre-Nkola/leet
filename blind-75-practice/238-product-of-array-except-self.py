from typing import List
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums) )

        pre, sub = 1,1
        for i in range(len(nums)):
            res[i] = pre
            pre *=  nums[i]
        for i in range(len(nums)-1, -1,-1):
            res[i] = sub
            sub *= nums[i]
        return res
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
    

