class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mydict = {}
        
        for c in nums:
            mydict[c] = 1 + mydict.get(c,0)
        val = max(mydict.values())
        keys = [key for key, value in mydict.items() if value == val]
        return keys[0]
    
sol = Solution()
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))

