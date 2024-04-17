class Solution:
    def rob1(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    def rob(self, nums: list[int]):
        return max(nums[0],self.rob1(nums[1:]), self.rob1(nums[:-1]))

sol = Solution()

print(sol.rob2(nums = [2,3,2]))