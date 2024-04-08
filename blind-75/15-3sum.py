
# using 2 pointers
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1 , len(nums) -1
            while l < r:
                mysum = nums[i] + nums[l] + nums[r]
                if mysum > 0:
                    r -=1
                elif mysum < 0:
                    l +=1
                else:
                    print(mysum, [nums[i], nums[l], nums[r]])
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1
                    while nums[l] ==nums[l-1]  and l< r:
                        l += 1
        return res

# using hashmap
    
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         res = []
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n )
#             myset = set()
#             if 

sol = Solution()

print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))