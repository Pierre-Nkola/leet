from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        l,r = 0, len(nums) -1
        if nums[mid] == target:
            return mid
            # Check if the left half is sorted
        if nums[l] <= nums[mid]:
            # If target is in the left half
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # The right half must be sorted
        else:
            # If target is in the right half
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
            
            