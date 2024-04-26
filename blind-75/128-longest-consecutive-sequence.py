class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        myset = set(nums)
        for num in nums:
            if num -1 not in myset:
                length = 0
                while (num+ length) in myset:
                    length += 1
                longest = max(length, longest)
        return longest
    
sol = Solution()

print(sol.longestConsecutive(nums = [100,4,200,1,3,2]))
                