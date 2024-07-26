class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            res = max(res, i - l +1)
        return res
    
sol = Solution()

print(sol.lengthOfLongestSubstring("pwwkew"))