from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            maxSub = max(maxSub, curr_sum)
        return maxSub