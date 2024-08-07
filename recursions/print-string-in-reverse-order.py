# print a string in reverse order
# recursively and iteratively

class Solution:
    
    def printReverseRecursive(self, s: str) -> str:
        # base case
        if len(s) == 0:
            return s
        # recursive
        else:
            return s[-1] + self.printReverseRecursive(s[:-1])
        
    def printReverseSlicing(self, s: str):
        return s[::-1]
    
    def printReverseIteratative(self, s: str):
        t = ""
        for i in range(len(s)-1, -1,-1):
            t += s[i]
        return t
        # this one takes a list as input parameter
    def printReverseRecurArr(self, s: list):
        l, r = 0, len(s) -1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
sol = Solution()
s1 = ["h","e","l","l","o"]
# print(sol.printReverseRecursive("point"))
print(sol.printReverseRecurArr(s1))
print(s1)