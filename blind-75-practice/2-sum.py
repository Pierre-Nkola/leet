from typing import List
class Solution:
    def twoSum(self, arr: List, target:int) -> List[int]:
        mydict = {}
        for i in range(len(arr)):
            if target - arr[i] in mydict:
                return [i, mydict[target - arr[i] ]]
            mydict[arr[i]] = i
            

sol = Solution()
print(sol.twoSum(arr = [2,7,11,15], target = 9))