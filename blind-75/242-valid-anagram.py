class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 , str2 = {}, {}
        
        for item in s:
            str1[item] = 1 + str1.get(item, 0)
            
        for item in t:
            str2[item] = 1 + str2.get(item, 0)
        
        return str1 == str2

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))