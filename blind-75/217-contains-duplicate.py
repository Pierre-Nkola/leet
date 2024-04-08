class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mydict = {}
        for item in nums:
            if item in mydict:
                return True
            mydict[item] += 0
        return False
        

sol = Solution()

sol_res = sol.containsDuplicate(nums = [1,2,3,1])

print(sol_res)