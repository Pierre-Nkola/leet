class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    def rob2(self, nums: list[int]):
        arr1, arr2 = nums[1:], nums[:-1]
        return max(self.rob(arr1), self.rob(arr2))

sol = Solution()

print(sol.rob2(nums = [2,3,2]))