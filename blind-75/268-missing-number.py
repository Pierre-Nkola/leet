# brute force using extra space
# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#         res = list(range(len(nums)))
        
#         for i in res:
#             if i not in nums:
#                 return i
            


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))
    
sol = Solution()

print(sol.missingNumber(nums = [3,0,1]))

