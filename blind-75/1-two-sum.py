# The algo is has 3 steps:
#  1- initializa an empty dict. dict is used as keys in a dictionary are uniques
#  2- for every value, we check if the complement(target - value) is in the dict and return the current index and the value of the key if found.
#  3- we add an item in the dict with the value being the index


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mydict = {}

        for i in range(len(nums)):
            if target - nums[i] in mydict:
                return [i, mydict[target -nums[i]]]
            mydict[nums[i]] = i






sol = Solution()

sol_res = sol.twoSum(nums = [2,7,11,15], target = 9)

print(sol_res)